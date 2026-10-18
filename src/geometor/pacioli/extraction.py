"""Module for extracting folios (images, text, manifests) from De Divina Proportione scans."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Dict, List, Optional


DEFAULT_PDF_PATH = Path("divinaproportion00paci.pdf")
DEFAULT_OUTPUT_DIR = Path("resources/de_divina_proportione/paganini_1509")

# Structural section mapping for the 1509 Paganini edition (318 pages)
EDITION_SECTIONS = [
    {
        "id": "front_matter",
        "title": "Front Matter and Dedications",
        "start_page": 1,
        "end_page": 16,
        "description": "Title page, epigrams, dedication to Piero Soderini, Daniel Caietanus epistle, list of 61 bodies, and Tabula.",
    },
    {
        "id": "compendio",
        "title": "Part I: Compendio de Divina Proportione",
        "start_page": 17,
        "end_page": 61,
        "description": "Chapters I to LXXI: Dedication to Ludovico Sforza, 5 divine analogies, 13 miraculous effects of the golden ratio, Platonic & Archimedean solids, and measurements.",
    },
    {
        "id": "architectura",
        "title": "Part II: Tractato de l'Architectura",
        "start_page": 61,
        "end_page": 84,
        "description": "Dedication to Pacioli's disciples in Sansepolcro and Chapters I to XX on Vitruvian human proportion, columns, capitals, entablatures, and architecture.",
    },
    {
        "id": "libellus",
        "title": "Part III: Libellus in tres partiales tractatus divisus",
        "start_page": 85,
        "end_page": 136,
        "description": "Three mathematical treatises on the five regular bodies and dependent solids (vernacular translation of Piero della Francesca's Libellus).",
    },
    {
        "id": "alphabet",
        "title": "Appendix I: The Roman Geometric Alphabet",
        "start_page": 137,
        "end_page": 186,
        "description": "Proportional profile of the human head (Divina Proportio), geometric construction plates of classical Roman capital letters (A-Y), and Porta Speciosa.",
    },
    {
        "id": "polyhedra_plates",
        "title": "Appendix II: Polyhedra Plates by Leonardo da Vinci",
        "start_page": 187,
        "end_page": 310,
        "description": "Full-page woodcut illustrations designed by Leonardo da Vinci of regular, truncated, and elevated polyhedra in solid (planum) and skeletal (vacuum) forms (Plates I-LIX), plus architectural plates.",
    },
    {
        "id": "end_matter",
        "title": "End Matter and Arbor Proportionis",
        "start_page": 311,
        "end_page": 318,
        "description": "Arbor Proportio et Proportionalitas (Tree of Ratios and Proportions) and closing flyleaves.",
    },
]


def ensure_dir(path: Path) -> None:
    """Ensure directory exists."""
    path.mkdir(parents=True, exist_ok=True)


def extract_single_image(
    pdf_path: Path, page_num: int, output_dir: Path, dpi: int = 150, force: bool = False
) -> Path:
    """Extract a single page from PDF as a PNG image."""
    dest_path = output_dir / f"{page_num:04d}.png"
    if dest_path.exists() and not force and dest_path.stat().st_size > 0:
        return dest_path

    prefix = output_dir / f"temp_{page_num:04d}"
    cmd = [
        "pdftoppm",
        "-png",
        "-r",
        str(dpi),
        "-f",
        str(page_num),
        "-l",
        str(page_num),
        str(pdf_path),
        str(prefix),
    ]

    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Find the generated file (pdftoppm appends -<page>.png)
    candidates = list(output_dir.glob(f"temp_{page_num:04d}-*.png"))
    if not candidates:
        raise RuntimeError(f"Failed to extract page {page_num} image from {pdf_path}")

    shutil.move(candidates[0], dest_path)
    return dest_path


def extract_single_text(
    pdf_path: Path, page_num: int, output_dir: Path, force: bool = False
) -> Path:
    """Extract text from a single page of PDF."""
    dest_path = output_dir / f"{page_num:04d}.rst"
    if dest_path.exists() and not force and dest_path.stat().st_size > 0:
        return dest_path

    cmd = [
        "pdftotext",
        "-f",
        str(page_num),
        "-l",
        str(page_num),
        str(pdf_path),
        str(dest_path),
    ]

    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return dest_path


def extract_all(
    pdf_path: Path,
    output_dir: Path,
    start_page: int = 1,
    end_page: int = 318,
    dpi: int = 150,
    max_workers: int = 6,
    force: bool = False,
) -> None:
    """Extract page images and text for the entire volume in parallel."""
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found at {pdf_path}")

    ensure_dir(output_dir)
    pages = list(range(start_page, end_page + 1))
    total = len(pages)

    print(f"Extracting {total} folios from {pdf_path} into {output_dir}")
    print(f"  Resolution: {dpi} DPI | Workers: {max_workers}")

    # Extract images in parallel
    print("Extracting folio images...")
    completed_img = 0
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(
                extract_single_image, pdf_path, p, output_dir, dpi=dpi, force=force
            ): p
            for p in pages
        }
        for future in as_completed(futures):
            future.result()
            completed_img += 1
            if completed_img % 25 == 0 or completed_img == total:
                print(f"  Images: {completed_img}/{total} complete ({completed_img*100//total}%)")

    # Generate manifest and section structure
    generate_manifest(output_dir, start_page, end_page)
    generate_sections_index(output_dir)
    print("Extraction complete.")


def generate_manifest(output_dir: Path, start_page: int, end_page: int) -> None:
    """Generate pages.json manifest matching the Euclid format."""
    pages_data = []
    for p in range(start_page, end_page + 1):
        folio_str = f"{p:04d}"
        img_name = f"{folio_str}.png"
        rst_name = f"{folio_str}.rst"

        # Determine section for page
        section_id = "unknown"
        for s in EDITION_SECTIONS:
            if s["start_page"] <= p <= s["end_page"]:
                section_id = s["id"]
                break

        pages_data.append(
            {
                "page_num": p,
                "folio": folio_str,
                "section": section_id,
                "image": img_name,
                "text": rst_name,
            }
        )

    manifest = {
        "work": "de_divina_proportione",
        "edition": "paganini_1509",
        "total_pages": len(pages_data),
        "pages": pages_data,
    }

    manifest_path = output_dir / "pages.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print(f"Manifest written to {manifest_path}")


def generate_sections_index(output_dir: Path) -> None:
    """Generate sections.json index mapping sections and page ranges."""
    sections_path = output_dir / "sections.json"
    with open(sections_path, "w", encoding="utf-8") as f:
        json.dump(EDITION_SECTIONS, f, indent=2)
    print(f"Sections index written to {sections_path}")


def main() -> None:
    """CLI entry point for folio extraction."""
    parser = argparse.ArgumentParser(
        description="Extract folios (images, text, manifests) from De Divina Proportione PDF"
    )
    parser.add_argument(
        "--pdf",
        type=Path,
        default=DEFAULT_PDF_PATH,
        help=f"Path to PDF file (default: {DEFAULT_PDF_PATH})",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Output directory (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--start", type=int, default=1, help="Start page number (default: 1)"
    )
    parser.add_argument(
        "--end", type=int, default=318, help="End page number (default: 318)"
    )
    parser.add_argument(
        "--dpi", type=int, default=150, help="DPI resolution for images (default: 150)"
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=6,
        help="Number of parallel extraction workers (default: 6)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force re-extraction of existing files",
    )

    args = parser.parse_args()
    extract_all(
        pdf_path=args.pdf,
        output_dir=args.output,
        start_page=args.start,
        end_page=args.end,
        dpi=args.dpi,
        max_workers=args.workers,
        force=args.force,
    )


if __name__ == "__main__":
    main()
