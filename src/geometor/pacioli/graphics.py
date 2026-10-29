"""Module and CLI utility for graphic, initial cap, and content metadata extraction for Pacioli."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
from PIL import Image

try:
    import cv2
except ImportError:
    cv2 = None

try:
    import scipy.ndimage
except ImportError:
    scipy = None


ROMAN_MAP = {
    "I": 1, "II": 2, "III": 3, "IIII": 4, "IV": 4, "V": 5,
    "VI": 6, "VII": 7, "VIII": 8, "VIIII": 9, "IX": 9, "X": 10,
    "XI": 11, "XII": 12, "XIII": 13, "XIIII": 14, "XIV": 14, "XV": 15,
    "XVI": 16, "XVII": 17, "XVIII": 18, "XVIIII": 19, "XIX": 19, "XX": 20,
    "XXI": 21, "XXII": 22, "XXIII": 23, "XXIIII": 24, "XXIV": 24, "XXV": 25,
    "XXVI": 26, "XXVII": 27, "XXVIII": 28, "XXVIIII": 29, "XXIX": 29, "XXX": 30,
    "XXXI": 31, "XXXII": 32, "XXXIII": 33, "XXXIIII": 34, "XXXIV": 34, "XXXV": 35,
    "XXXVI": 36, "XXXVII": 37, "XXXVIII": 38, "XXXVIIII": 39, "XXXIX": 39, "XL": 40,
    "XLI": 41, "XLII": 42, "XLIII": 43, "XLIIII": 44, "XLIV": 44, "XLV": 45,
    "XLVI": 46, "XLVII": 47, "XLVIII": 48, "XLVIIII": 49, "XLIX": 49, "L": 50,
    "LI": 51, "LII": 52, "LIII": 53, "LIIII": 54, "LIV": 54, "LV": 55,
    "LVI": 56, "LVII": 57, "LVIII": 58, "LVIIII": 59, "LIX": 59, "LX": 60,
    "LXI": 61, "LXII": 62, "LXIII": 63, "LXIIII": 64, "LXIV": 64, "LXV": 65,
    "LXVI": 66, "LXVII": 67, "LXVIII": 68, "LXVIIII": 69, "LXIX": 69, "LXX": 70,
    "LXXI": 71,
}


def clean_image(
    pil_image: Image.Image,
    white_point: int = 226,
    preserve_color: bool = False,
) -> Image.Image:
    """Normalize aged parchment background and binding shadows to pure white (255).

    Uses morphological closing + Gaussian blur to estimate local paper illumination per channel,
    eliminating yellowed paper cast, bleed-through, and gutter shadows while preserving crisp ink.
    When ``preserve_color=True`` (e.g., red rubrication on folios 0005 and 0311), chromatic ink is kept.
    """
    rgb_img = pil_image.convert("RGB")
    arr = np.array(rgb_img, dtype=np.float32)

    if cv2 is not None and arr.shape[0] >= 16 and arr.shape[1] >= 16:
        ksize = min(31, max(7, (min(arr.shape[0], arr.shape[1]) // 4) | 1))
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (ksize, ksize))
        bg = cv2.morphologyEx(arr, cv2.MORPH_CLOSE, kernel)
        bsize = min(51, max(11, (min(arr.shape[0], arr.shape[1]) // 2) | 1))
        bg = cv2.GaussianBlur(bg, (bsize, bsize), 0)
        p85 = np.percentile(arr, 85, axis=(0, 1))
        scale = float(white_point) / 235.0
        wp = np.minimum(bg, p85 * 1.02) * scale
    else:
        p85 = np.percentile(arr, 85, axis=(0, 1))
        wp = np.maximum(p85 * (float(white_point) / 235.0), 120.0)

    bp = 28.0
    norm = np.clip((arr - bp) * 255.0 / np.maximum(wp - bp, 40.0), 0.0, 255.0)

    if not preserve_color and pil_image.mode != "L":
        gray = 0.299 * norm[:, :, 0] + 0.587 * norm[:, :, 1] + 0.114 * norm[:, :, 2]
        cleaned_np = np.stack([gray, gray, gray], axis=-1).astype(np.uint8)
    elif pil_image.mode == "L":
        gray = 0.299 * norm[:, :, 0] + 0.587 * norm[:, :, 1] + 0.114 * norm[:, :, 2]
        cleaned_np = gray.astype(np.uint8)
    else:
        cleaned_np = norm.astype(np.uint8)

    cleaned_pil = Image.fromarray(cleaned_np)
    if pil_image.mode != cleaned_pil.mode:
        cleaned_pil = cleaned_pil.convert(pil_image.mode)
    return cleaned_pil



def find_text_column_bounds(gray: np.ndarray, is_recto: bool) -> Tuple[int, int]:
    """Dynamically locate the horizontal [x_left, x_right] bounds of the main printed text column."""
    h_img, w_img = gray.shape
    bw = (gray < 170).astype(np.float32)
    col_density = bw[100 : h_img - 100, :].mean(axis=0)

    if is_recto:
        # On odd (recto) pages, find the rightmost column of the dense text block in x=[400..655]
        text_right_cols = np.where(col_density[400:655] > 0.12)[0]
        x_right = (400 + int(text_right_cols[-1])) if len(text_right_cols) else 610
        x_left = max(18, x_right - 548)
    else:
        # On even (verso) pages, find the leftmost column of the dense text block in x=[350..550]
        text_left_cols = np.where(col_density[350:550] > 0.12)[0]
        x_left = (350 + int(text_left_cols[0])) if len(text_left_cols) else 395
        x_right = min(w_img - 15, x_left + 548)

    return x_left, x_right


def detect_initials(image_path: Path) -> List[Dict[str, Any]]:
    """Detect woodcut illuminated initial caps by finding 2D ink-density centers along the text column edge.

    Woodcut initials in the 1509 Paganini edition have consistent square dimensions:
    - Standard chapter initials: 120x132 px (padded around the ~112x118 woodcut frame)
    - Large treatise-opening initials (folios 0017 and 0085): 260x304 px
    - Title-page red initial D (folio 0005): 184x188 px
    """
    if scipy is None:
        return []

    stem = image_path.stem
    if not stem.isdigit():
        return []
    page_num = int(stem)
    if page_num <= 4 or page_num == 6 or page_num == 84 or page_num >= 136:
        return []

    try:
        gray = np.array(Image.open(str(image_path)).convert("L"))
    except Exception:
        return []

    h_img, w_img = gray.shape
    bw = (gray < 165).astype(np.float32)

    if page_num == 5:
        roi = (gray[130:350, 200:410] < 185).astype(np.float32)
        dens = scipy.ndimage.uniform_filter(roi, size=150, mode="constant")
        max_val = float(dens.max())
        if max_val < 0.35:
            return []
        ys, xs = np.where(dens >= 0.90 * max_val)
        cx, cy = int(np.mean(xs)), int(np.mean(ys))
        W, H = 184, 188
        return [
            {
                "x_offset": int(200 + cx - W // 2),
                "y_offset": int(130 + cy - H // 2),
                "crop_box": [int(W), int(H)],
                "size_class": "title",
            }
        ]

    is_recto = page_num % 2 == 1
    x_min, x_max = (24, 330) if is_recto else (370, 560)
    y_min, y_max = 50, h_img - 55
    sub = bw[y_min:y_max, x_min:x_max]

    results: List[Dict[str, Any]] = []
    work = sub.copy()

    # 1. Large treatise-opening initials (folios 0017 and 0085): 260x304
    if page_num in (17, 85):
        dens_large = scipy.ndimage.uniform_filter(work, size=(270, 230), mode="constant")
        while True:
            max_val = float(dens_large.max())
            if max_val < 0.62:
                break
            cy_peak, cx_peak = np.unravel_index(np.argmax(dens_large), dens_large.shape)
            r1, r2 = max(0, int(cy_peak) - 50), min(work.shape[0], int(cy_peak) + 50)
            c1, c2 = max(0, int(cx_peak) - 50), min(work.shape[1], int(cx_peak) + 50)
            local = dens_large[r1:r2, c1:c2]
            ys, xs = np.where(local >= 0.92 * max_val)
            cy = int(r1 + int(np.mean(ys)))
            cx = int(c1 + int(np.mean(xs)))
            W, H = 264, 304
            gx = int(max(0, x_min + cx - W // 2 - 6))
            gy = int(max(0, y_min + cy - H // 2))
            results.append(
                {
                    "x_offset": gx,
                    "y_offset": gy,
                    "crop_box": [int(W), int(H)],
                    "size_class": "large",
                }
            )
            zr1, zr2 = max(0, cy - 150), min(work.shape[0], cy + 150)
            work[zr1:zr2, :] = 0
            dens_large = scipy.ndimage.uniform_filter(work, size=(270, 230), mode="constant")

    # 2. Standard chapter initials: 124x132 centered on 2D ink-density centroid
    dens_std = scipy.ndimage.uniform_filter(work, size=(114, 104), mode="constant")
    while True:
        max_val = float(dens_std.max())
        if max_val < 0.65:
            break
        cy_peak, cx_peak = np.unravel_index(np.argmax(dens_std), dens_std.shape)
        r1, r2 = max(0, int(cy_peak) - 25), min(work.shape[0], int(cy_peak) + 25)
        c1, c2 = max(0, int(cx_peak) - 25), min(work.shape[1], int(cx_peak) + 25)
        local = dens_std[r1:r2, c1:c2]
        ys, xs = np.where(local >= 0.93 * max_val)
        cy = int(r1 + int(np.mean(ys)))
        cx = int(c1 + int(np.mean(xs)))
        W, H = 124, 132
        gx = int(max(0, x_min + cx - W // 2 - 4))
        gy = int(max(0, y_min + cy - H // 2))
        results.append(
            {
                "x_offset": gx,
                "y_offset": gy,
                "crop_box": [int(W), int(H)],
                "size_class": "standard",
            }
        )
        # Suppress only the 116px height of the found initial so closely stacked initials are not clipped
        zr1, zr2 = max(0, cy - 58), min(work.shape[0], cy + 58)
        work[zr1:zr2, :] = 0
        dens_std = scipy.ndimage.uniform_filter(work, size=(114, 104), mode="constant")

    results.sort(key=lambda r: r["y_offset"])
    return results


def detect_margin_figures(image_path: Path, is_recto: bool) -> List[Dict[str, Any]]:
    """Detect geometric diagrams and marginalia strictly in the outer margin of a text folio.

    - Odd (recto) folios: right outer margin (to the right of the main text column).
    - Even (verso) folios: left outer margin (to the left of the main text column).
    Never falls back to full-page text blocks.
    """
    if scipy is None:
        return []

    try:
        gray = np.array(Image.open(str(image_path)).convert("L"))
    except Exception:
        return []

    height, width = gray.shape
    x_text_left, x_text_right = find_text_column_bounds(gray, is_recto=is_recto)

    if is_recto:
        margin_x1 = max(int(width * 0.58), x_text_right + 12)
        margin_x2 = width - 18
        margin_side = "right"
    else:
        margin_x1 = 18
        margin_x2 = min(int(width * 0.41), x_text_left - 12)
        margin_side = "left"

    if margin_x2 <= margin_x1 + 30:
        return []

    margin_y1, margin_y2 = 45, height - 65
    margin_gray = gray[margin_y1:margin_y2, margin_x1:margin_x2]

    binary = margin_gray < 165
    closed = scipy.ndimage.binary_closing(binary, structure=np.ones((3, 3)))
    labels, _ = scipy.ndimage.label(closed, structure=np.ones((3, 3)))
    slices = scipy.ndimage.find_objects(labels)

    boxes = []
    for sl in slices:
        if sl is None:
            continue
        y1, y2 = sl[0].start, sl[0].stop
        x1, x2 = sl[1].start, sl[1].stop
        h = y2 - y1
        w = x2 - x1
        if h < 12 and w < 12:
            continue
        if w < 10 and (x1 < 8 or x2 > (margin_x2 - margin_x1 - 8)):
            continue
        comp_gray = margin_gray[y1:y2, x1:x2]
        dark_pixels = int((comp_gray < 140).sum())
        if dark_pixels < 10:
            continue
        boxes.append([x1, y1, x2, y2])

    if not boxes:
        return []

    # Merge nearby labels/components belonging to the same figure using closest-pair
    # agglomerative clustering, without merging distinct vertically stacked diagrams.
    while True:
        best_pair = None
        best_dist = 1e9
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                ax1, ay1, ax2, ay2 = boxes[i]
                bx1, by1, bx2, by2 = boxes[j]
                ah, bh = ay2 - ay1, by2 - by1
                aw, bw_box = ax2 - ax1, bx2 - bx1
                v_dist = max(0, max(ay1, by1) - min(ay2, by2))
                h_dist = max(0, max(ax1, bx1) - min(ax2, bx2))

                # Two large figures stacked vertically should stay separate
                both_large = (ah >= 85 and aw >= 70) and (bh >= 85 and bw_box >= 70)
                if both_large:
                    should_merge = (v_dist == 0 and h_dist < 15)
                else:
                    # Merge small corner labels (a, b, c, d, numbers) into adjacent diagram
                    should_merge = (v_dist < 24 and h_dist < 65) or (v_dist < 8 and h_dist < 85)

                if should_merge:
                    dist = v_dist * 3.0 + h_dist
                    if dist < best_dist:
                        best_dist = dist
                        best_pair = (i, j)

        if best_pair is None:
            break
        i, j = best_pair
        ax1, ay1, ax2, ay2 = boxes[i]
        bx1, by1, bx2, by2 = boxes[j]
        boxes[i] = [
            min(ax1, bx1),
            min(ay1, by1),
            max(ax2, bx2),
            max(ay2, by2),
        ]
        boxes.pop(j)

    boxes.sort(key=lambda b: (b[1], b[0]))

    results = []
    PADDING = 14
    for x1, y1, x2, y2 in boxes:
        cw = x2 - x1
        ch = y2 - y1
        if cw < 38 and ch < 38:
            continue
        roi_gray = margin_gray[y1:y2, x1:x2]
        very_dark = int((roi_gray < 125).sum())
        if very_dark < 65:
            continue

        black_ink = int((roi_gray < 95).sum())
        is_diagram = black_ink >= 140 and (cw >= 55 or ch >= 75)
        gtype = "diagram" if is_diagram else "marginalia"

        gx = max(0, margin_x1 + x1 - PADDING)
        gy = max(0, margin_y1 + y1 - PADDING)
        gw = min(width - gx, cw + 2 * PADDING)
        gh = min(height - gy, ch + 2 * PADDING)
        results.append(
            {
                "x_offset": int(gx),
                "y_offset": int(gy),
                "crop_box": [int(gw), int(gh)],
                "type": gtype,
                "margin": margin_side,
            }
        )

    return results


def detect_graphics_scipy(image_path: Path) -> List[Dict[str, Any]]:
    """Detect full-page plate woodcuts on a folio (137-309) using NumPy and SciPy."""
    if scipy is None:
        return []

    try:
        pil_img = Image.open(str(image_path)).convert("L")
    except Exception:
        return []

    gray = np.array(pil_img)
    height, width = gray.shape

    hist, _ = np.histogram(gray, bins=256, range=(0, 256))
    total = gray.size
    sum_total = np.dot(np.arange(256), hist)
    curr_max, thresh = 0.0, 0
    wb, sb = 0, 0.0
    for i in range(256):
        wb += int(hist[i])
        if wb == 0:
            continue
        wf = total - wb
        if wf == 0:
            break
        sb += float(i * hist[i])
        mb = sb / wb
        mf = (sum_total - sb) / wf
        var_b = float(wb) * float(wf) * (mb - mf) ** 2
        if var_b > curr_max:
            curr_max = var_b
            thresh = i

    binary = gray < thresh
    labels, _ = scipy.ndimage.label(binary, structure=np.ones((3, 3)))
    slices = scipy.ndimage.find_objects(labels)

    MIN_GRAPHIC_DIM = 60
    MAX_TEXT_HEIGHT = 40
    MIN_TEXT_WIDTH = 100

    large_components = []
    core_mask = np.zeros_like(binary, dtype=bool)

    for idx, sl in enumerate(slices):
        if sl is None:
            continue
        h = sl[0].stop - sl[0].start
        w = sl[1].stop - sl[1].start
        if w > MIN_TEXT_WIDTH and h < MAX_TEXT_HEIGHT:
            continue
        if w > MIN_GRAPHIC_DIM or h > MIN_GRAPHIC_DIM:
            large_components.append(idx + 1)
            core_mask[labels == (idx + 1)] = True

    if not large_components:
        return []

    pts_y, pts_x = np.where(core_mask)
    gx, gy = pts_x.min(), pts_y.min()
    gw, gh = pts_x.max() - gx + 1, pts_y.max() - gy + 1

    PADDING = 15
    gx = max(0, int(gx - PADDING))
    gy = max(0, int(gy - PADDING))
    gw = min(width - gx, int(gw + 2 * PADDING))
    gh = min(height - gy, int(gh + 2 * PADDING))

    return [{"x_offset": gx, "y_offset": gy, "crop_box": [gw, gh], "type": "plate"}]


def detect_graphics_cv(image_path: Path) -> List[Dict[str, Any]]:
    """Detect full-page plate graphics using OpenCV if available, falling back to SciPy."""
    if cv2 is None:
        return detect_graphics_scipy(image_path)

    img = cv2.imread(str(image_path))
    if img is None:
        return []

    height, width = img.shape[:2]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    num_labels, _, stats, _ = cv2.connectedComponentsWithStats(binary, connectivity=8)

    MIN_GRAPHIC_DIM = 60
    MIN_CORE_HEIGHT = 38

    cores = []
    for i in range(1, num_labels):
        x = int(stats[i, cv2.CC_STAT_LEFT])
        y = int(stats[i, cv2.CC_STAT_TOP])
        w = int(stats[i, cv2.CC_STAT_WIDTH])
        h = int(stats[i, cv2.CC_STAT_HEIGHT])
        if h < MIN_CORE_HEIGHT:
            continue
        if w > MIN_GRAPHIC_DIM or h > MIN_GRAPHIC_DIM:
            cores.append([x, y, w, h, [i]])

    if not cores:
        return []

    merged = True
    while merged:
        merged = False
        for i in range(len(cores)):
            for j in range(i + 1, len(cores)):
                x1, y1, w1, h1, ids1 = cores[i]
                x2, y2, w2, h2, ids2 = cores[j]
                v_dist = max(0, max(y1, y2) - min(y1 + h1, y2 + h2))
                h_dist = max(0, max(x1, x2) - min(x1 + w1, x2 + w2))
                if (v_dist == 0 and h_dist < 85) or (h_dist == 0 and v_dist < 25):
                    nx = min(x1, x2)
                    ny = min(y1, y2)
                    nw = max(x1 + w1, x2 + w2) - nx
                    nh = max(y1 + h1, y2 + h2) - ny
                    cores[i] = [nx, ny, nw, nh, ids1 + ids2]
                    cores.pop(j)
                    merged = True
                    break
            if merged:
                break

    cores.sort(key=lambda c: (c[1], c[0]))
    PADDING = 15
    results = []
    for cx, cy, cw, ch, _ in cores:
        gx = max(0, cx - PADDING)
        gy = max(0, cy - PADDING)
        gw = min(width - gx, cw + 2 * PADDING)
        gh = min(height - gy, ch + 2 * PADDING)
        results.append(
            {"x_offset": int(gx), "y_offset": int(gy), "crop_box": [int(gw), int(gh)], "type": "plate"}
        )
    return results


def detect_graphics_folio(image_path: Path) -> List[Dict[str, Any]]:
    """Context-aware graphic detection based on folio page number and book section."""
    stem = image_path.stem
    if not stem.isdigit():
        return detect_graphics_cv(image_path)

    page_num = int(stem)
    is_recto = page_num % 2 == 1

    # Blank flyleaves, frontmatter/tabula (1-16), and blank pages
    if page_num <= 16 or page_num in (84, 136) or page_num >= 312:
        return []

    # 1. Polyhedra Plates (187 - 309), Alphabet/Architecture Plates (137 - 186), & Arbor Proportionis (311):
    # Odd pages are full-page woodcuts; even pages are blank backs of plates.
    if 137 <= page_num <= 311:
        if not is_recto:
            return []
        return detect_graphics_cv(image_path)

    # 2. Treatises (17 - 135):
    # Diagrams and marginalia are strictly in the outer margin (right on recto, left on verso).
    return detect_margin_figures(image_path, is_recto=is_recto)


def load_winterberg_chapters(resources_root: Path) -> Dict[Tuple[int, int], Dict[str, Any]]:
    """Load clean Italian, German, and English chapter titles and file links from Winterberg resources."""
    mapping: Dict[Tuple[int, int], Dict[str, Any]] = {}
    wb_dir = resources_root / "winterberg"
    en_dir = resources_root / "winterberg_en" / "divina_en_2"

    # Book 1: Divina Proportione (Chapters 1..71)
    it1_dir = wb_dir / "01_divina_proportione_italian"
    de1_dir = wb_dir / "03_divina_proportione_german"
    if it1_dir.exists():
        for f in sorted(it1_dir.glob("*.txt")):
            m = re.match(r"^(\d+)_", f.name)
            if not m:
                continue
            cnum = int(m.group(1))
            if cnum == 0:
                continue
            lines = [ln.strip() for ln in f.read_text(encoding="utf-8", errors="ignore").splitlines() if ln.strip()]
            heading_it = lines[1] if len(lines) > 1 and lines[0].lower().startswith(("cap", "gap")) else (lines[0] if lines else "")
            entry: Dict[str, Any] = {
                "book": 1,
                "chapter": cnum,
                "title_it": heading_it,
                "winterberg_it": f"winterberg/01_divina_proportione_italian/{f.name}",
            }
            de_match = list(de1_dir.glob(f"{cnum:03d}_*.txt")) if de1_dir.exists() else []
            if de_match:
                entry["winterberg_de"] = f"winterberg/03_divina_proportione_german/{de_match[0].name}"
            en_match = list(en_dir.glob(f"{cnum:03d}_*.txt")) if en_dir.exists() else []
            if en_match:
                en_lines = [ln.strip() for ln in en_match[0].read_text(encoding="utf-8", errors="ignore").splitlines() if ln.strip()]
                entry["title_en"] = en_lines[0].lstrip("# ").strip() if en_lines else ""
                entry["winterberg_en"] = f"winterberg_en/divina_en_2/{en_match[0].name}"
            mapping[(1, cnum)] = entry

    # Book 2: Tractato de Architectura (Chapters 1..20)
    it2_dir = wb_dir / "02_architectura_italian"
    de2_dir = wb_dir / "04_architectura_german"
    if it2_dir.exists():
        for f in sorted(it2_dir.glob("*_cap_*.txt")):
            m = re.match(r"^(\d+)_cap_([IVXLCDM]+)\.txt$", f.name)
            if not m:
                continue
            cnum = ROMAN_MAP.get(m.group(2), int(m.group(1)))
            lines = [ln.strip() for ln in f.read_text(encoding="utf-8", errors="ignore").splitlines() if ln.strip()]
            heading_it = lines[1] if len(lines) > 1 and lines[0].lower().startswith(("cap", "gap")) else (lines[0] if lines else "")
            entry = {
                "book": 2,
                "chapter": cnum,
                "title_it": heading_it,
                "winterberg_it": f"winterberg/02_architectura_italian/{f.name}",
            }
            de_match = list(de2_dir.glob(f"*_cap_{m.group(2)}.txt")) if de2_dir.exists() else []
            if de_match:
                entry["winterberg_de"] = f"winterberg/04_architectura_german/{de_match[0].name}"
            mapping[(2, cnum)] = entry

    return mapping


def extract_folio_content_info(
    folio_num: int,
    folio_dir: Path,
    wb_map: Optional[Dict[Tuple[int, int], Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """Determine book part, recto/verso side, running header, and chapters/cases on a folio."""
    side = "recto" if folio_num % 2 == 1 else "verso"
    if folio_num <= 4:
        section = "Flyleaf"
        book_num = 0
    elif folio_num == 5:
        section = "Title Page"
        book_num = 0
    elif folio_num == 6:
        section = "Epigrams and Sonnets"
        book_num = 0
    elif 7 <= folio_num <= 10:
        section = "Dedication and Laudatory Epigrams"
        book_num = 0
    elif 11 <= folio_num <= 16:
        section = "Tabula (Table of Contents)"
        book_num = 0
    elif 17 <= folio_num <= 61:
        section = "Part I: Compendio de Divina Proportione"
        book_num = 1
    elif 62 <= folio_num <= 83:
        section = "Part II: Tractato de l'Architectura"
        book_num = 2
    elif folio_num == 84:
        section = "Blank Folio"
        book_num = 2
    elif 85 <= folio_num <= 136:
        section = "Part III: Libellus in tres partiales tractatus divisus"
        book_num = 3
    elif 137 <= folio_num <= 186:
        section = "Appendix I: The Roman Geometric Alphabet"
        book_num = 4
    elif 187 <= folio_num <= 310:
        section = "Appendix II: Polyhedra Plates by Leonardo da Vinci"
        book_num = 5
    else:
        section = "End Matter and Colophon"
        book_num = 0

    info: Dict[str, Any] = {
        "side": side,
        "section": section,
    }

    rst_path = folio_dir / f"{folio_num:04d}.rst"
    txt_path = folio_dir / f"{folio_num:04d}.txt"
    source_path = rst_path if rst_path.exists() else txt_path
    if not source_path.exists():
        return info

    raw_text = source_path.read_text(encoding="utf-8", errors="ignore")
    lines = [ln.strip() for ln in raw_text.splitlines() if ln.strip() and not ln.strip().startswith(":")]
    if lines:
        info["header"] = lines[0][:60]

    chapters: List[Dict[str, Any]] = []
    if book_num == 1 and folio_num == 17:
        if wb_map and (1, 1) in wb_map:
            chapters.append(wb_map[(1, 1)])
        else:
            chapters.append({"book": 1, "chapter": 1, "title_it": "Epistola a Ludovico Maria Sforza"})

    # Detect Cap. <Roman> or Casus <Number> in the OCR text
    if book_num in (1, 2):
        # Match patterns like "Cap. XIII." or "Cap. XIIII." or "Ca. XX."
        for m in re.finditer(r"\b(?:Cap|Ca|Gap)[\.,\s]+([IVXLCDM]+)\b", raw_text):
            roman = m.group(1).upper()
            if roman in ROMAN_MAP:
                cnum = ROMAN_MAP[roman]
                if wb_map and (book_num, cnum) in wb_map:
                    entry = dict(wb_map[(book_num, cnum)])
                else:
                    entry = {"book": book_num, "chapter": cnum, "roman": roman}
                if not any(c.get("chapter") == cnum for c in chapters):
                    chapters.append(entry)
    elif book_num == 3:
        for m in re.finditer(r"\b(?:Casus|Lafus|Cafus)[\.,\s]+([0-9]+|primus|secundus|tertius)\b", raw_text, re.IGNORECASE):
            casus_id = m.group(1)
            chapters.append({"book": 3, "casus": casus_id})

    if chapters:
        info["chapters"] = chapters

    return info


def detect_single_image(
    img_path: Path,
    save: bool = False,
    force: bool = False,
    wb_map: Optional[Dict[Tuple[int, int], Dict[str, Any]]] = None,
) -> Optional[Dict[str, Any]]:
    """Detect margin graphics, illuminated initial caps, and content info on a single folio scan."""
    if not img_path.exists():
        print(f"Error: image not found at {img_path}", file=sys.stderr)
        return None

    folio_stem = img_path.stem
    json_path = img_path.with_name(f"{folio_stem}.json")
    if save and json_path.exists() and not force:
        print(f"Skipping {json_path} (already exists). Use --force to overwrite.")
        return None

    if wb_map is None and img_path.parent.parent.exists():
        wb_map = load_winterberg_chapters(img_path.parent.parent)

    page_num = int(folio_stem) if folio_stem.isdigit() else 0
    content_info = extract_folio_content_info(page_num, img_path.parent, wb_map=wb_map) if page_num else {}

    # 1. Detect Margin Graphics (or Plates on 137-309)
    graphic_results = detect_graphics_folio(img_path)
    graphics = []
    for idx, result in enumerate(graphic_results, start=1):
        gid = f"g{idx}"
        x = result["x_offset"]
        y = result["y_offset"]
        w, h = result["crop_box"]
        gtype = result.get("type", "diagram")
        g_entry: Dict[str, Any] = {
            "id": gid,
            "type": gtype,
            "file": f"{folio_stem}.{gid}.png",
            "bbox": [x, y, w, h],
            "white_point": 226,
            "caption": f"Folio {folio_stem} {'Diagram' if gtype == 'diagram' else gtype.capitalize()} {idx}",
        }
        if "margin" in result:
            g_entry["margin"] = result["margin"]
        graphics.append(g_entry)

    # 2. Detect Illuminated Initial Caps (0005 - 0135) and store in graphics list
    initial_results = detect_initials(img_path)
    for idx, result in enumerate(initial_results, start=1):
        cid = f"c{idx}"
        x = result["x_offset"]
        y = result["y_offset"]
        w, h = result["crop_box"]
        graphics.append(
            {
                "id": cid,
                "type": "initial",
                "size_class": result.get("size_class", "standard"),
                "file": f"{folio_stem}.{cid}.png",
                "bbox": [x, y, w, h],
                "white_point": 226,
                "caption": f"Folio {folio_stem} Initial Cap {idx}",
            }
        )

    metadata: Dict[str, Any] = {
        "folio": folio_stem,
        **content_info,
        "graphics": graphics,
    }
    output_json = json.dumps(metadata, indent=2, ensure_ascii=False)

    if not save:
        print(output_json)
    else:
        with open(json_path, "w", encoding="utf-8") as f:
            f.write(output_json + "\n")
        n_diag = sum(1 for g in graphics if g.get("type") != "initial")
        n_init = sum(1 for g in graphics if g.get("type") == "initial")
        print(
            f"Saved {json_path.name}: {n_diag} margin graphic(s), {n_init} initial cap(s)"
        )
    return metadata


def extract_from_json(json_path: Path, no_clean: bool = False) -> None:
    """Extract all margin graphics and illuminated initial caps defined in <folio>.json."""
    if not json_path.exists():
        print(f"Error: JSON file not found at {json_path}", file=sys.stderr)
        return

    with open(json_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"Error parsing JSON {json_path}: {e}", file=sys.stderr)
            return

    folio = data.get("folio", json_path.stem)
    all_items = list(data.get("graphics", [])) + list(data.get("initials", []))

    img_path = json_path.with_name(f"{folio}.png")
    if not img_path.exists():
        print(f"Error: Source image not found at {img_path}", file=sys.stderr)
        return

    if not all_items:
        return

    img = Image.open(img_path)
    img_w, img_h = img.size

    for item in all_items:
        gid = item.get("id", "g1")
        bbox = item.get("bbox")
        if not bbox or len(bbox) != 4:
            continue

        x, y, w, h = bbox
        crop_box = (max(0, x), max(0, y), min(img_w, x + w), min(img_h, y + h))
        cropped = img.crop(crop_box)

        white_point = item.get("white_point", 226)
        if not no_clean and white_point is not None:
            preserve_color = bool(item.get("preserve_color", folio in ("0005", "0311")))
            cropped = clean_image(
                cropped,
                white_point=white_point,
                preserve_color=preserve_color,
            )

        out_name = item.get("file", f"{folio}.{gid}.png")
        out_path = json_path.parent / out_name
        cropped.save(out_path)

        print(f"  Extracted {folio}.{gid} ({item.get('type', 'graphic')}): bbox={bbox} -> {out_name}")


def build_graphics_index(directory: Path) -> Path:
    """Compile all per-folio <folio>.json files into graphics_index.json."""
    section_map = {
        "Flyleaf": ("frontmatter", "Frontmatter & Tabula"),
        "Title Page": ("frontmatter", "Frontmatter & Tabula"),
        "Dedication and Laudatory Epigrams": ("frontmatter", "Frontmatter & Tabula"),
        "Tabula (Table of Contents)": ("frontmatter", "Frontmatter & Tabula"),
        "Pars Prima: Compendio de Divina Proportione": ("compendio", "Part I: Compendio de Divina Proportione"),
        "Pars Secunda: Tractato de Architectura": ("architectura", "Part II: Tractato de Architectura"),
        "Blank Folio": ("architectura", "Part II: Tractato de Architectura"),
        "Pars Tertia: Libellus in tres partiales tractatus divisus": ("libellus", "Part III: Libellus in tres partiales tractatus divisus"),
        "Appendix I: Roman Alphabet Plates": ("alphabet_plates", "Appendix I: Roman Alphabet Plates"),
        "Appendix II: Polyhedra Plates by Leonardo da Vinci": ("polyhedra_plates", "Appendix II: Polyhedra Plates by Leonardo da Vinci"),
    }
    index_entries: List[Dict[str, Any]] = []
    for jf in sorted(directory.glob("*.json")):
        if not jf.stem.isdigit():
            continue
        try:
            with open(jf, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            continue

        folio = data.get("folio", jf.stem)
        page_num = int(folio)
        sec_key = data.get("section", "")
        if not sec_key:
            if page_num <= 16:
                sec_key = "Tabula (Table of Contents)"
            elif page_num <= 63:
                sec_key = "Pars Prima: Compendio de Divina Proportione"
            elif page_num <= 84:
                sec_key = "Pars Secunda: Tractato de Architectura"
            elif page_num <= 135:
                sec_key = "Pars Tertia: Libellus in tres partiales tractatus divisus"
            elif page_num <= 185:
                sec_key = "Appendix I: Roman Alphabet Plates"
            else:
                sec_key = "Appendix II: Polyhedra Plates by Leonardo da Vinci"

        section_id, section_title = section_map.get(sec_key, (sec_key, sec_key))
        side = data.get("side", "recto" if page_num % 2 == 1 else "verso")
        header = data.get("header", "")
        chapters = data.get("chapters", [])

        for item in data.get("graphics", []):
            entry: Dict[str, Any] = {
                "folio": folio,
                "page_num": page_num,
                "side": side,
                "section_id": section_id,
                "section_title": section_title,
                "id": item.get("id", "g1"),
                "type": item.get("type", "plate" if page_num >= 137 else "diagram"),
                "file": item.get("file", f"{folio}.{item.get('id', 'g1')}.png"),
                "bbox": item.get("bbox", []),
                "white_point": item.get("white_point", 226),
                "caption": item.get("caption", ""),
            }
            if "margin" in item:
                entry["margin"] = item["margin"]
            if "size_class" in item:
                entry["size_class"] = item["size_class"]
            if "letter" in item:
                entry["letter"] = item["letter"]
            if header:
                entry["header"] = header
            if chapters:
                entry["chapters"] = chapters
            index_entries.append(entry)

    out_path = directory / "graphics_index.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(index_entries, f, indent=2, ensure_ascii=False)
    print(f"Built {out_path} with {len(index_entries)} items across folios.")
    return out_path


def main() -> None:
    """CLI for managing graphics and illuminated initials in Pacioli folios."""
    parser = argparse.ArgumentParser(description="Pacioli Graphic & Initial Cap Detection and Extraction Tool")
    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    # detect
    p_detect = subparsers.add_parser("detect", help="Detect graphics and initials on folio image(s)")
    p_detect.add_argument("targets", nargs="+", help="Image files or directories")
    p_detect.add_argument("--save", action="store_true", help="Save results to <folio>.json")
    p_detect.add_argument("--force", action="store_true", help="Overwrite existing <folio>.json")
    p_detect.add_argument("--max-folio", type=int, default=135, help="Max folio number when scanning a directory (default: 135)")

    # extract
    p_extract = subparsers.add_parser("extract", help="Extract graphics and initials defined in <folio>.json")
    p_extract.add_argument("targets", nargs="+", help="JSON files, PNG files, or directories")
    p_extract.add_argument("--no-clean", action="store_true", help="Disable white-point cleaning")
    p_extract.add_argument("--max-folio", type=int, default=135, help="Max folio number when extracting a directory (default: 135)")

    # index
    p_index = subparsers.add_parser("index", help="Build graphics_index.json from <folio>.json files in directory")
    p_index.add_argument("directory", help="Directory containing <folio>.json files")

    # set
    p_set = subparsers.add_parser("set", help="Set or update a graphic or initial in <folio>.json")
    p_set.add_argument("target", help="Target folio stem, PNG, or JSON path")
    p_set.add_argument("--id", default="g1", help="ID (e.g. g1, g2 for graphics; c1, c2 for initials)")
    p_set.add_argument("--type", default=None, help="Type (diagram, marginalia, initial, plate)")
    p_set.add_argument("--bbox", nargs=4, type=int, required=True, metavar=("X", "Y", "W", "H"))
    p_set.add_argument("--caption", default="", help="Caption for graphic/initial")
    p_set.add_argument("--letter", default="", help="Letter for initial cap (e.g. C, S, E, L)")
    p_set.add_argument("--white-point", type=int, default=226, help="White point (default: 226)")
    p_set.add_argument("--extract", action="store_true", help="Immediately extract after setting")

    args = parser.parse_args()

    if args.subcommand == "detect":
        for target_str in args.targets:
            target = Path(target_str)
            if target.is_dir():
                wb_map = load_winterberg_chapters(target.parent)
                for pf in sorted(target.glob("*.png")):
                    if pf.stem.isdigit() and int(pf.stem) <= args.max_folio:
                        detect_single_image(pf, save=args.save, force=args.force, wb_map=wb_map)
                if args.save:
                    build_graphics_index(target)
            elif target.suffix == ".png":
                detect_single_image(target, save=args.save, force=args.force)

    elif args.subcommand == "extract":
        for target_str in args.targets:
            target = Path(target_str)
            if target.is_dir():
                for jf in sorted(target.glob("*.json")):
                    if jf.stem.isdigit() and int(jf.stem) <= args.max_folio:
                        extract_from_json(jf, no_clean=args.no_clean)
            elif target.suffix == ".json":
                extract_from_json(target, no_clean=args.no_clean)
            elif target.suffix == ".png":
                jf = target.with_suffix(".json")
                if jf.exists():
                    extract_from_json(jf, no_clean=args.no_clean)

    elif args.subcommand == "index":
        build_graphics_index(Path(args.directory))

    elif args.subcommand == "set":
        target = Path(args.target)
        folio = target.stem
        json_path = target.with_name(f"{folio}.json") if target.suffix else Path(f"{args.target}.json")
        metadata: Dict[str, Any] = {}
        if json_path.exists():
            try:
                with open(json_path, "r", encoding="utf-8") as f:
                    metadata = json.load(f)
            except Exception:
                metadata = {}
        metadata["folio"] = folio
        is_initial = args.id.startswith("c") or args.type == "initial"
        items = metadata.get("graphics", [])
        item_type = args.type or ("initial" if is_initial else "diagram")
        entry: Dict[str, Any] = {
            "id": args.id,
            "type": item_type,
            "file": f"{folio}.{args.id}.png",
            "bbox": list(args.bbox),
            "white_point": args.white_point,
            "caption": args.caption or f"Folio {folio} {'Initial Cap' if is_initial else 'Figure'} {args.id.lstrip('gc')}",
        }
        if args.letter:
            entry["letter"] = args.letter
        items = [it for it in items if it.get("id") != args.id]
        items.append(entry)
        metadata["graphics"] = items
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        print(f"Updated {json_path} with {args.id} ({item_type}): bbox={args.bbox}")
        if args.extract:
            extract_from_json(json_path)


if __name__ == "__main__":
    main()
