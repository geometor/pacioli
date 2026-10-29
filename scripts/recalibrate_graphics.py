#!/usr/bin/env python3
"""Recalibrate bounding boxes, remove false-positive detections, and re-extract clean graphics for Paganini 1509."""

from __future__ import annotations

import json
import re
from pathlib import Path

import cv2
import numpy as np

from geometor.pacioli.graphics import build_graphics_index, extract_from_json

FOLIO_DIR = Path("resources/de_divina_proportione/paganini_1509")

# False-positive marginal "diagrams" / "marginalia" (table columns, creases, reader scribbles)
FALSE_POSITIVE_G_IDS = {
    "0007": {"g1"},
    "0008": {"g1"},
    "0009": {"g1", "g2"},
    "0010": {"g1", "g2", "g3"},
    "0011": {"g1", "g2", "g3", "g4"},
    "0012": {"g1"},
    "0013": {"g1", "g2"},
    "0014": {"g1", "g2"},
    "0015": {"g1", "g2"},
    "0016": {"g1", "g2", "g3"},
    "0017": {"g1"},
    "0019": {"g1"},
    "0020": {"g1"},
    "0026": {"g1"},
    "0059": {"g1"},
    "0066": {"g2"},
    "0313": {"g1"},
}

# Exact hand-verified overrides for special diagrams and full-page architectural plates
EXACT_BBOX_OVERRIDES = {
    ("0036", "g1"): [28, 196, 342, 564],
    ("0066", "g1"): [162, 365, 358, 626],
    ("0069", "g1"): [775, 62, 85, 1205],
    ("0085", "c1"): [20, 189, 264, 298],
    ("0137", "g1"): [48, 32, 825, 1404],
    ("0185", "g1"): [38, 12, 995, 1420],
    ("0213", "g1"): [42, 16, 914, 1370],
    ("0215", "g1"): [18, 105, 1000, 1134],
    ("0311", "g1"): [25, 10, 1085, 1410],
}


def compute_binary_ink(gray: np.ndarray, thresh_diff: int = 32) -> np.ndarray:
    """Compute local-background-subtracted binary ink mask immune to binding shadows."""
    bg = cv2.GaussianBlur(gray, (101, 101), 0)
    binary = ((bg.astype(np.int16) - gray.astype(np.int16)) > thresh_diff).astype(np.uint8) * 255
    return binary


def recalibrate_plate_woodcut(gray: np.ndarray, page_num: int) -> list[int]:
    """Compute tight bounding box around the woodcut illustration on Alphabet (139-183) or Polyhedra (187-309) plates."""
    h, w = gray.shape
    mask = compute_binary_ink(gray, thresh_diff=32)

    # Remove left page edge and any tall vertical binding crease in x < 38
    mask[:, :10] = 0
    gutter_zone = mask[:, :38]
    v_band = cv2.morphologyEx(gutter_zone, cv2.MORPH_OPEN, np.ones((35, 1), np.uint8))
    v_band = cv2.dilate(v_band, np.ones((9, 5), np.uint8))
    mask[:, :38] = cv2.subtract(gutter_zone, v_band)

    if 187 <= page_num <= 309:
        # Exclude movable-type Greek top header, right vertical transliteration, and bottom Latin title
        mask[:120, :] = 0
        mask[:, 890:] = 0
        mask[955:, :] = 0
    elif 139 <= page_num <= 183:
        # Exclude movable-type Italian paragraph below the alphabet woodcut frame
        mask[:95, :] = 0
        mask[:, 920:] = 0
        mask[965:, :] = 0

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    dil = cv2.dilate(mask, kernel, iterations=1)
    num_labels, _, stats, _ = cv2.connectedComponentsWithStats(dil, connectivity=8)
    if num_labels <= 1:
        return [100, 200, 600, 600]

    best_i = max(range(1, num_labels), key=lambda i: int(stats[i, cv2.CC_STAT_AREA]))
    cx = int(stats[best_i, cv2.CC_STAT_LEFT])
    cy = int(stats[best_i, cv2.CC_STAT_TOP])
    cw = int(stats[best_i, cv2.CC_STAT_WIDTH])
    ch = int(stats[best_i, cv2.CC_STAT_HEIGHT])

    pad = 12
    x1 = max(6, cx - pad)
    y1 = max(12, cy - pad)
    x2 = min(w - 12, cx + cw + pad)
    y2 = min(h - 12, cy + ch + pad)
    return [int(x1), int(y1), int(x2 - x1), int(y2 - y1)]


def recalibrate_marginal_diagrams(
    folio: str,
    gray: np.ndarray,
    side: str,
    g_items: list[dict],
) -> None:
    """Recalibrate marginal diagram bboxes using local text-gap detection and vertical midpoint splitting."""
    if not g_items:
        return

    h_img, w_img = gray.shape
    binary = (compute_binary_ink(gray, thresh_diff=30) > 0).astype(np.uint8)
    # Mask out outermost 8px page edges
    binary[:, :8] = 0
    binary[:, w_img - 8 :] = 0

    # First pass: expand top (if previously clamped at y=32) and inner x (if clamped before local text gap)
    raw_ink_bounds: list[list[int]] = []
    for item in g_items:
        gid = item["id"]
        if (folio, gid) in EXACT_BBOX_OVERRIDES:
            ox, oy, ow, oh = EXACT_BBOX_OVERRIDES[(folio, gid)]
            raw_ink_bounds.append([ox, oy, ox + ow, oy + oh])
            continue

        x, y, w, h = item["bbox"]
        x1, y1, x2, y2 = x, y, x + w, y + h

        # If y1 was clamped at 32, allow searching up to y=2
        if y1 <= 36:
            y1 = 2

        # Find local text-column gap in [y1..y2]
        band = binary[max(0, y1) : min(h_img, y2), :]
        col_proj = band.sum(axis=0)
        if side == "verso":
            # Diagram is in left margin; text is to the right
            gap_x = x2
            for cx in range(min(w_img - 1, x2 - 12), min(w_img - 1, 520)):
                if col_proj[cx] == 0 and col_proj[max(0, cx - 2) : min(w_img, cx + 3)].sum() == 0:
                    gap_x = cx
                    break
            x2 = max(x2, gap_x)
        else:
            # Diagram is in right margin; text is to the left
            gap_x = x1
            for cx in range(max(0, x1 + 12), max(0, 520), -1):
                if col_proj[cx] == 0 and col_proj[max(0, cx - 2) : min(w_img, cx + 3)].sum() == 0:
                    gap_x = cx
                    break
            x1 = min(x1, gap_x)

        # Find tight ink bounds inside [x1..x2, y1..y2]
        sub = binary[y1:y2, x1:x2]
        ys, xs = np.where(sub > 0)
        if len(xs) > 0:
            ix1 = x1 + int(xs.min())
            iy1 = y1 + int(ys.min())
            ix2 = x1 + int(xs.max()) + 1
            iy2 = y1 + int(ys.max()) + 1
        else:
            ix1, iy1, ix2, iy2 = x1, y1, x2, y2
        raw_ink_bounds.append([ix1, iy1, ix2, iy2])

    # Second pass: apply padding while clamping vertical neighbors at their empty gap midpoint
    pad = 10
    for idx, item in enumerate(g_items):
        gid = item["id"]
        if (folio, gid) in EXACT_BBOX_OVERRIDES:
            item["bbox"] = list(EXACT_BBOX_OVERRIDES[(folio, gid)])
            continue

        ix1, iy1, ix2, iy2 = raw_ink_bounds[idx]
        bx1 = max(4, ix1 - pad)
        by1 = max(2, iy1 - pad)
        bx2 = min(w_img - 4, ix2 + pad)
        by2 = min(h_img - 2, iy2 + pad)

        # Check vertical overlap with previous diagram on same folio
        if idx > 0 and (folio, g_items[idx - 1]["id"]) not in EXACT_BBOX_OVERRIDES:
            prev_ix1, prev_iy1, prev_ix2, prev_iy2 = raw_ink_bounds[idx - 1]
            # Only clamp if they overlap horizontally (stacked in the same column)
            if min(ix2, prev_ix2) > max(ix1, prev_ix1):
                if by1 < prev_iy2 + pad:
                    # Find minimum horizontal projection row between prev_iy2 - 6 and iy1 + 6
                    s_y1 = max(0, min(prev_iy2, iy1) - 8)
                    s_y2 = min(h_img, max(prev_iy2, iy1) + 8)
                    if s_y2 > s_y1:
                        row_proj = binary[s_y1:s_y2, min(ix1, prev_ix1) : max(ix2, prev_ix2)].sum(axis=1)
                        zero_rows = np.where(row_proj == row_proj.min())[0]
                        split_y = s_y1 + int(np.median(zero_rows))
                    else:
                        split_y = (prev_iy2 + iy1) // 2
                    by1 = max(by1, split_y)
                    # Also clamp previous item's height
                    prev_bbox = g_items[idx - 1]["bbox"]
                    prev_bbox[3] = min(prev_bbox[3], max(10, split_y - prev_bbox[1]))

        item["bbox"] = [int(bx1), int(by1), int(bx2 - bx1), int(by2 - by1)]


def remove_false_positives_from_rst(folio: str, removed_ids: set[str]) -> None:
    """Remove .. picture:: <folio>.<gid>.png directives for deleted false-positive graphics in <folio>.rst."""
    rst_path = FOLIO_DIR / f"{folio}.rst"
    if not rst_path.exists():
        return
    text = rst_path.read_text(encoding="utf-8")
    orig = text
    for gid in sorted(removed_ids):
        pattern = rf"\.\. picture:: {re.escape(folio)}\.{re.escape(gid)}\.png\n(?:   :[^\n]+\n)*\n*"
        text = re.sub(pattern, "", text)
    if text != orig:
        rst_path.write_text(text, encoding="utf-8")


def main() -> None:
    removed_count = 0
    recalibrated_count = 0

    for jf in sorted(FOLIO_DIR.glob("*.json")):
        if not jf.stem.isdigit():
            continue
        folio = jf.stem
        page_num = int(folio)
        data = json.loads(jf.read_text(encoding="utf-8"))
        graphics = data.get("graphics", [])
        if not graphics:
            continue

        # 1. Remove false-positive g items
        bad_ids = FALSE_POSITIVE_G_IDS.get(folio, set())
        if bad_ids:
            kept = []
            for g in graphics:
                if g["id"] in bad_ids:
                    png_file = FOLIO_DIR / g.get("file", f"{folio}.{g['id']}.png")
                    if png_file.exists():
                        png_file.unlink()
                    removed_count += 1
                else:
                    kept.append(g)
            graphics = kept
            data["graphics"] = graphics
            remove_false_positives_from_rst(folio, bad_ids)

        if not graphics:
            jf.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            continue

        img_path = FOLIO_DIR / f"{folio}.png"
        if not img_path.exists():
            continue
        gray = cv2.imread(str(img_path), cv2.IMREAD_GRAYSCALE)
        if gray is None:
            continue

        side = data.get("side", "recto" if page_num % 2 == 1 else "verso")

        # Apply exact overrides to c items if any (e.g., 0085.c1)
        for item in graphics:
            key = (folio, item["id"])
            if key in EXACT_BBOX_OVERRIDES:
                item["bbox"] = list(EXACT_BBOX_OVERRIDES[key])

        g_items = [g for g in graphics if g["id"].startswith("g")]
        if g_items:
            if 137 <= page_num <= 311:
                for g in g_items:
                    key = (folio, g["id"])
                    if key in EXACT_BBOX_OVERRIDES:
                        g["bbox"] = list(EXACT_BBOX_OVERRIDES[key])
                    else:
                        g["bbox"] = recalibrate_plate_woodcut(gray, page_num)
                    recalibrated_count += 1
            else:
                recalibrate_marginal_diagrams(folio, gray, side, g_items)
                recalibrated_count += len(g_items)

        jf.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        extract_from_json(jf)

    build_graphics_index(FOLIO_DIR)
    conc_path = FOLIO_DIR / "concordance.json"
    if conc_path.exists():
        conc = json.loads(conc_path.read_text(encoding="utf-8"))
        for fnum in range(1, 319):
            fstr = f"{fnum:04d}"
            fj = FOLIO_DIR / f"{fstr}.json"
            if fj.exists() and fstr in conc.get("folios", {}):
                conc["folios"][fstr]["graphics"] = json.loads(fj.read_text(encoding="utf-8")).get("graphics", [])
        conc_path.write_text(json.dumps(conc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Done: removed {removed_count} false positives, recalibrated & extracted {recalibrated_count} graphics.")


if __name__ == "__main__":
    main()
