"""Module and CLI utility for graphic detection, cropping, and managing <folio>.json for Pacioli."""

from __future__ import annotations

import argparse
import json
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


def clean_image(pil_image: Image.Image, white_point: int = 226) -> Image.Image:
    """Applies a linear levels adjustment to the image, mapping white_point to pure white (255).

    Effectively eliminates bleed-through, yellowed paper background, and scanning artifacts.
    """
    if pil_image.mode in ("RGB", "L"):
        img_np = np.array(pil_image)
    else:
        img_np = np.array(pil_image.convert("RGB"))

    lut = np.zeros((256,), dtype=np.uint8)
    for i in range(256):
        if i >= white_point:
            val = 255
        else:
            val = i * 255.0 / white_point
        lut[i] = np.clip(val, 0, 255)

    if cv2 is not None:
        cleaned_np = cv2.LUT(img_np, lut)
    else:
        cleaned_np = lut[img_np]

    cleaned_pil = Image.fromarray(cleaned_np)
    if pil_image.mode != cleaned_pil.mode:
        cleaned_pil = cleaned_pil.convert(pil_image.mode)
    return cleaned_pil


def detect_graphics_scipy(image_path: Path) -> List[Dict[str, Any]]:
    """Detect diagrams/figures on a folio using pure NumPy and SciPy."""
    if scipy is None:
        return []

    try:
        pil_img = Image.open(str(image_path)).convert("L")
    except Exception:
        return []

    gray = np.array(pil_img)
    height, width = gray.shape

    # Otsu thresholding
    hist, _ = np.histogram(gray, bins=256, range=(0, 256))
    total = gray.size
    sum_total = np.dot(np.arange(256), hist)
    curr_max, thresh = 0, 0
    wb, sb = 0, 0
    for i in range(256):
        wb += hist[i]
        if wb == 0:
            continue
        wf = total - wb
        if wf == 0:
            break
        sb += i * hist[i]
        mb = sb / wb
        mf = (sum_total - sb) / wf
        var_b = wb * wf * (mb - mf) ** 2
        if var_b > curr_max:
            curr_max = var_b
            thresh = i

    binary = gray < thresh

    # Connected components
    labels, num_labels = scipy.ndimage.label(binary, structure=np.ones((3, 3)))
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

    return [{"x_offset": gx, "y_offset": gy, "crop_box": [gw, gh]}]


def detect_graphics_cv(image_path: Path) -> List[Dict[str, Any]]:
    """Detect graphics using OpenCV if available, falling back to SciPy."""
    if cv2 is None:
        return detect_graphics_scipy(image_path)

    img = cv2.imread(str(image_path))
    if img is None:
        return []

    height, width = img.shape[:2]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(binary, connectivity=8)

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

    # Merge overlapping cores
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
    for cx, cy, cw, ch, cids in cores:
        gx = max(0, cx - PADDING)
        gy = max(0, cy - PADDING)
        gw = min(width - gx, cw + 2 * PADDING)
        gh = min(height - gy, ch + 2 * PADDING)
        results.append({"x_offset": int(gx), "y_offset": int(gy), "crop_box": [int(gw), int(gh)]})
    return results


def detect_margin_figures(image_path: Path, is_recto: bool) -> List[Dict[str, Any]]:
    """Detect distinct geometric diagrams in the outer margin of a text folio."""
    if scipy is None:
        return []

    try:
        pil_img = Image.open(str(image_path)).convert("L")
    except Exception:
        return []

    gray = np.array(pil_img)
    height, width = gray.shape

    # Outer margins:
    # Recto (odd page): right margin (x: 580 to width - 30)
    # Verso (even page): left margin (x: 30 to 450)
    if is_recto:
        margin_x1, margin_x2 = int(width * 0.58), width - 20
    else:
        margin_x1, margin_x2 = 20, int(width * 0.44)

    margin_y1, margin_y2 = 40, height - 80
    margin = gray[margin_y1:margin_y2, margin_x1:margin_x2]
    binary = margin < 185

    labels, num_labels = scipy.ndimage.label(binary, structure=np.ones((3, 3)))
    slices = scipy.ndimage.find_objects(labels)

    boxes = []
    for sl in slices:
        if sl is None:
            continue
        h = sl[0].stop - sl[0].start
        w = sl[1].stop - sl[1].start
        # Filter noise/speckles and single isolated letters
        if (h > 35 or w > 35) and not (w < 25 and h < 25):
            boxes.append([sl[1].start, sl[0].start, sl[1].stop, sl[0].stop])

    if not boxes:
        return []

    # Sort boxes top to bottom
    boxes.sort(key=lambda b: b[1])

    # Cluster components that are close vertically (gap < 40px)
    clusters = []
    for b in boxes:
        if not clusters:
            clusters.append(b)
        else:
            prev = clusters[-1]
            if b[1] - prev[3] < 40:
                prev[0] = min(prev[0], b[0])
                prev[1] = min(prev[1], b[1])
                prev[2] = max(prev[2], b[2])
                prev[3] = max(prev[3], b[3])
            else:
                clusters.append(b)

    results = []
    PADDING = 12
    for x1, y1, x2, y2 in clusters:
        cw = x2 - x1
        ch = y2 - y1
        # Ignore very tiny slivers or single small numbers
        if cw < 30 and ch < 30:
            continue
        gx = max(0, margin_x1 + x1 - PADDING)
        gy = max(0, margin_y1 + y1 - PADDING)
        gw = min(width - gx, cw + 2 * PADDING)
        gh = min(height - gy, ch + 2 * PADDING)
        results.append({"x_offset": int(gx), "y_offset": int(gy), "crop_box": [int(gw), int(gh)]})

    return results


def detect_graphics_folio(image_path: Path) -> List[Dict[str, Any]]:
    """Context-aware graphic detection based on folio page number and book section."""
    stem = image_path.stem
    if not stem.isdigit():
        return detect_graphics_cv(image_path)

    page_num = int(stem)
    is_recto = (page_num % 2 == 1)

    # 1. Polyhedra Plates (187 - 314):
    # Odd pages are full-page woodcuts by Leonardo da Vinci.
    # Even pages are blank backs of plates.
    if 187 <= page_num <= 314:
        if not is_recto:
            return []  # Blank verso
        # Detect the large central woodcut
        return detect_graphics_cv(image_path)

    # 2. Alphabet Plates (136 - 186):
    # Odd pages contain the woodcut letters and construction text
    if 136 <= page_num <= 186:
        if not is_recto:
            return []  # Blank verso
        return detect_graphics_cv(image_path)

    # 3. Libellus on Regular Bodies (85 - 135) & Compendio (17 - 80):
    # Geometric diagrams are printed in the outer margin.
    if 17 <= page_num <= 135:
        margin_res = detect_margin_figures(image_path, is_recto=is_recto)
        if margin_res:
            return margin_res
        # Fall back to general detection if no margin figures found
        return detect_graphics_cv(image_path)

    # Default general detection
    return detect_graphics_cv(image_path)


def detect_single_image(img_path: Path, save: bool = False, force: bool = False) -> None:
    """Detect graphic bounding box(es) on a single folio scan and optionally save <folio>.json."""
    if not img_path.exists():
        print(f"Error: image not found at {img_path}", file=sys.stderr)
        return

    folio_stem = img_path.stem
    json_path = img_path.with_name(f"{folio_stem}.json")
    if save and json_path.exists() and not force:
        print(f"Skipping {json_path} (already exists). Use --force to overwrite.")
        return

    results = detect_graphics_folio(img_path)
    graphics = []
    for idx, result in enumerate(results, start=1):
        gid = f"g{idx}"
        x = result["x_offset"]
        y = result["y_offset"]
        w, h = result["crop_box"]
        graphics.append(
            {
                "id": gid,
                "file": f"{folio_stem}.{gid}.png",
                "bbox": [x, y, w, h],
                "white_point": 226,
                "caption": f"Folio {folio_stem} Figure {idx}",
            }
        )

    metadata = {"folio": folio_stem, "graphics": graphics}
    output_json = json.dumps(metadata, indent=2)

    if not save:
        print(output_json)
    else:
        with open(json_path, "w", encoding="utf-8") as f:
            f.write(output_json + "\n")
        print(f"Saved {json_path} ({len(graphics)} graphic(s))")


def extract_from_json(json_path: Path, no_clean: bool = False) -> None:
    """Extract all graphics defined in a <folio>.json file from the corresponding folio scan."""
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
    graphics = data.get("graphics", [])

    img_path = json_path.with_name(f"{folio}.png")
    if not img_path.exists():
        print(f"Error: Source image not found at {img_path}", file=sys.stderr)
        return

    if not graphics:
        print(f"Folio {folio}: No graphics defined in {json_path.name}")
        return

    img = Image.open(img_path)
    img_w, img_h = img.size

    for g in graphics:
        gid = g.get("id", "g1")
        bbox = g.get("bbox")
        if not bbox or len(bbox) != 4:
            continue

        x, y, w, h = bbox
        crop_box = (max(0, x), max(0, y), min(img_w, x + w), min(img_h, y + h))
        cropped = img.crop(crop_box)

        white_point = g.get("white_point", 226)
        if not no_clean and white_point is not None:
            cropped = clean_image(cropped, white_point=white_point)

        out_name = g.get("file", f"{folio}.{gid}.png")
        out_path = json_path.parent / out_name
        cropped.save(out_path)

        print(f"  Extracted {folio}.{gid}: bbox={bbox} -> {out_name}")


def main() -> None:
    """CLI for managing graphics in Pacioli folios."""
    parser = argparse.ArgumentParser(description="Pacioli Graphic Detection and Extraction Tool")
    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    # detect
    p_detect = subparsers.add_parser("detect", help="Detect graphics on folio image(s)")
    p_detect.add_argument("targets", nargs="+", help="Image files or directories")
    p_detect.add_argument("--save", action="store_true", help="Save results to <folio>.json")
    p_detect.add_argument("--force", action="store_true", help="Overwrite existing <folio>.json")

    # extract
    p_extract = subparsers.add_parser("extract", help="Extract graphics defined in <folio>.json")
    p_extract.add_argument("targets", nargs="+", help="JSON files, PNG files, or directories")
    p_extract.add_argument("--no-clean", action="store_true", help="Disable white-point cleaning")

    # set
    p_set = subparsers.add_parser("set", help="Set or update graphic metadata in <folio>.json")
    p_set.add_argument("target", help="Target folio stem, PNG, or JSON path")
    p_set.add_argument("--id", default="g1", help="Graphic ID (default: g1)")
    p_set.add_argument("--bbox", nargs=4, type=int, required=True, metavar=("X", "Y", "W", "H"))
    p_set.add_argument("--caption", default="", help="Caption for graphic")
    p_set.add_argument("--white-point", type=int, default=226, help="White point (default: 226)")
    p_set.add_argument("--extract", action="store_true", help="Immediately extract after setting")

    args = parser.parse_args()

    if args.subcommand == "detect":
        for target_str in args.targets:
            target = Path(target_str)
            if target.is_dir():
                for pf in sorted(target.glob("*.png")):
                    if pf.stem.isdigit():
                        detect_single_image(pf, save=args.save, force=args.force)
            elif target.suffix == ".png":
                detect_single_image(target, save=args.save, force=args.force)

    elif args.subcommand == "extract":
        for target_str in args.targets:
            target = Path(target_str)
            if target.is_dir():
                for jf in sorted(target.glob("*.json")):
                    if jf.stem.isdigit():
                        extract_from_json(jf, no_clean=args.no_clean)
            elif target.suffix == ".json":
                extract_from_json(target, no_clean=args.no_clean)
            elif target.suffix == ".png":
                jf = target.with_suffix(".json")
                if jf.exists():
                    extract_from_json(jf, no_clean=args.no_clean)

    elif args.subcommand == "set":
        target = Path(args.target)
        folio = target.stem
        json_path = target.with_name(f"{folio}.json") if target.suffix else Path(f"{args.target}.json")
        metadata = {}
        if json_path.exists():
            try:
                with open(json_path, "r", encoding="utf-8") as f:
                    metadata = json.load(f)
            except Exception:
                metadata = {}
        metadata["folio"] = folio
        graphics = metadata.get("graphics", [])
        entry = {
            "id": args.id,
            "file": f"{folio}.{args.id}.png",
            "bbox": list(args.bbox),
            "white_point": args.white_point,
            "caption": args.caption or f"Folio {folio} Figure {args.id.replace('g', '')}",
        }
        graphics = [g for g in graphics if g.get("id") != args.id]
        graphics.append(entry)
        metadata["graphics"] = graphics
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2)
        print(f"Updated {json_path} with graphic {args.id}: bbox={args.bbox}")
        if args.extract:
            extract_from_json(json_path)


if __name__ == "__main__":
    main()
