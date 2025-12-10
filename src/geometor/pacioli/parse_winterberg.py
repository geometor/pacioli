import re
import shutil
from pathlib import Path
from typing import List

def clean_lines(lines: List[str]) -> List[str]:
    """
    Remove page artifacts and clean text.
    """
    cleaned = []
    # Patterns to remove
    # Page markers: ## p. 123 (#123)
    p_page = re.compile(r"^##\s+p\.\s+\d+.*$")
    # Headers
    p_header_1 = re.compile(r"^Quellenschriften f\. Kunstgesch.*$")
    p_header_2 = re.compile(r"^WINTERBERG.*$")
    p_header_3 = re.compile(r"^DIVINA PROPORTIONE.*$")
    # Loose page numbers (36o, i66, 172) - strict or context based?
    # Context based is hard line-by-line. Let's try strict for known patterns.
    # Single small words that are digits or like 'i66' on a line by themselves?
    p_loose_num = re.compile(r"^\s*(\d+|i\d+|[1-9]o)\s*$") # 36o, i66

    for line in lines:
        if p_page.match(line):
            continue
        if p_header_1.match(line):
            continue
        if p_header_2.match(line):
            continue
        if p_header_3.match(line):
            continue
        if p_loose_num.match(line):
            continue
        
        # Skip form feeds
        if '\f' in line:
            line = line.replace('\f', '')
            if not line.strip(): # if line is empty after removing form feed
                continue
        
        # Clean leading spaces (OCR artifact)
        # We use lstrip(' ') to remove leading spaces but preserve indentation if it was tabs (unlikely here)
        # actually, just removing *one* space might be what they asked, but usually OCR puts 1 space.
        # lstrip() handles 1 or more. 
        line = line.lstrip(' ')
        
        # We can add more specific cleaning rules here if needed
        # For now, we keep the text relatively raw but free of the navigation artifacts
        
        cleaned.append(line)
        
    return cleaned

def parse_winterberg():
    """
    Parses the Winterberg text file into top-level sections.
    """
    source_path = Path("resources/de_divina_proportione/winterberg.txt")
    output_dir = Path("resources/de_divina_proportione/winterberg")
    
    # Always clear output directory first
    if output_dir.exists():
        print(f"Clearing output directory: {output_dir}")
        shutil.rmtree(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    with open(source_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    print(f"Total lines: {len(lines)}")
    
    # Define Split Points
    
    idx_italian_start = -1
    idx_italian_arch = -1
    idx_german_start = -1
    idx_german_arch = -1
    idx_notes = -1
    idx_plates = -1
    
    for i, line in enumerate(lines):
        # User defined split point: --- followed shortly by Divina proportione
        if line.strip() == "Divina proportione" and idx_italian_start == -1:
             # The --- is usually 2 lines before (line 752)
             # But let's just use the "Divina proportione" line or slightly before if we see the ---
             if i > 2 and lines[i-2].strip() == "---":
                 idx_italian_start = i - 2
             else:
                 idx_italian_start = i
        
        # Architecture Start (Italian) - ## p. 123
        if "## p. 123 (#135)" in line:
            idx_italian_arch = i
             
        # German Start - ## p. 164
        if "## p. 164 (#176)" in line:
            idx_german_start = i

        # Architecture Start (German) - Dedication "Seinen theuersten Schülern"
        if "Seinen theuersten Schülern" in line and idx_german_arch == -1:
             # Just to be safe, searching for the dedication line
             idx_german_arch = i
            
        if "## p. 338 (#350)" in line:
            idx_notes = i
            
        if "## p. 351 (#363)" in line:
            idx_plates = i
            
    # Fallback to hardcoded if not found
    if idx_italian_start == -1: idx_italian_start = 751
    if idx_italian_arch == -1: idx_italian_arch = 5272
    if idx_german_start == -1: idx_german_start = 7111
    if idx_german_arch == -1: idx_german_arch = 12899
    if idx_notes == -1: idx_notes = 15197
    if idx_plates == -1: idx_plates = 15950
    
    print(f"Split indices: {idx_italian_start}, {idx_italian_arch}, {idx_german_start}, {idx_german_arch}, {idx_notes}, {idx_plates}")
    
    sections = {
        "00_intro.txt": lines[:idx_italian_start],
        "01_divina_proportione_italian.txt": lines[idx_italian_start:idx_italian_arch],
        "02_architectura_italian.txt": lines[idx_italian_arch:idx_german_start],
        "03_divina_proportione_german.txt": lines[idx_german_start:idx_german_arch],
        "04_architectura_german.txt": lines[idx_german_arch:idx_notes],
        "05_notes.txt": lines[idx_notes:idx_plates],
        "06_plates.txt": lines[idx_plates:]
    }
    
    print("Writing sections...")
    for filename, content_lines in sections.items():
        cleaned = clean_lines(content_lines)
        out_file = output_dir / filename
        with open(out_file, 'w', encoding='utf-8') as out:
            out.writelines(cleaned)
        print(f"Wrote {filename}: {len(cleaned)} lines")
        
        # Split intro
        if filename == "00_intro.txt":
            split_intro(cleaned, output_dir)

        # Split into chapters if it is a book file
        if "divina_proportione" in filename or "architectura" in filename:
            book_dir = output_dir / out_file.stem
            book_dir.mkdir(parents=True, exist_ok=True)
            print(f"Splitting {filename} into chapters in {book_dir}...")
            split_book_into_chapters(cleaned, book_dir, filename)

def split_intro(lines: List[str], output_dir: Path):
    """
    Splits the intro file into metadata, title page, and introduction.
    """
    intro_dir = output_dir / "00_intro"
    intro_dir.mkdir(parents=True, exist_ok=True)
    
    # Simple split based on "---" separation we saw in file
    # Metadata is at top. Title page starts after first ---
    # Introduction starts after second ---, or we can look for specific text.
    
    # Based on view_file:
    # Line 32: ---
    # Line 40: QUELLENSCHRIFTEN (Title page start)
    # The second part seems to be the german title page and info.
    # The actual introduction text starts later?
    # Line 700+ is introduction.
    
    # Let's try to split by the "---" markers.
    parts = []
    current_part = []
    for line in lines:
        if line.strip() == "---":
            parts.append(current_part)
            current_part = []
        else:
            current_part.append(line)
    parts.append(current_part)
    
    # Part 0: Metadata
    # Part 1: Title Info
    # Part 2: More Title Info / Intro start?
    
    # Let's just write what we have found for now as 000_metadata, 001_front_matter...
    # Refinement:
    # Metadata matches lines 1-31
    # Title Page matches lines 40-99
    
    if len(parts) > 0:
        (intro_dir / "000_metadata.txt").write_text("".join(parts[0]), encoding="utf-8")
    if len(parts) > 1:
        (intro_dir / "001_title_page.txt").write_text("".join(parts[1]), encoding="utf-8")
    if len(parts) > 2:
        # Join the rest as introduction
        intro_text = []
        for p in parts[2:]:
            intro_text.extend(p)
            intro_text.append("\n---\n") # keep marker
        (intro_dir / "002_introduction.txt").write_text("".join(intro_text), encoding="utf-8")


def split_book_into_chapters(lines: List[str], output_dir: Path, filename: str):
    """
    Split book lines into chapter files.
    """
    chapters = []
    current_lines = []
    current_title = "000_toc" # Default first section is TOC
    
    # Regex for chapter headers: Cap. I., Gap. III., etc.
    p_chapter = re.compile(r"^\s*(?:[CG]ap|Cup|Cüp)[.,]?\s+([IVXLCDM]+|ili)\.?", re.IGNORECASE)
    
    # Markers for Text Body Start
    is_italian_book_1 = "01_divina_proportione_italian" in filename
    is_german_book_1 = "03_divina_proportione_german" in filename
    is_arch_italian = "02_architectura_italian" in filename
    is_arch_german = "04_architectura_german" in filename
    
    # Italian Start: "Excellentissimo principi Ludouico"
    # German Start: "Brief von der göttlichen Proportion" (approx) or "Ludwig Maria Sforza"
    
    body_started = False
    
    # Architecture books start immediately with dedication/text
    if is_arch_italian or is_arch_german:
        body_started = True
        current_title = "000_dedication"

    for i, line in enumerate(lines):
        # Check for Body Start for Divina Proportione books
        start_body = False
        if is_italian_book_1 and not body_started:
             if "Excellentissimo principi Ludouico" in line:
                 start_body = True
        elif is_german_book_1 and not body_started:
             # Using a substring that is definitely in the start title
             if "Ludwig Maria Sforza" in line and "Herzog von Mailand" in line:
                 start_body = True
        
        if start_body:
             body_started = True
             # Save current (TOC)
             if current_lines:
                 chapters.append((current_title, current_lines))
             
             # Start Body Intro (Dedication/Epistola)
             current_title = "000_dedication"
             current_lines = [line]
             continue

        # Check for Chapter Header ONLY if body has started (or if we want TOC chapters?)
        # User wants "Separate TOC from Text body".
        # So we should probably NOT split TOC by 'Cap.' lines inside the TOC.
        # But 'Cap.' lines in TOC are list items.
        # Only split matches if body_started is True.
        
        
        match = p_chapter.match(line)
        if match and body_started:
            # Check for trailing title in previous chapter
            next_subtitle = None
            if current_lines:
                subtitle_lines, visited_lines = extract_trailing_title(current_lines)
                if subtitle_lines:
                    # Remove subtitle from current_lines
                    # We need to rebuild current_lines without the subtitle lines
                    # The extract_trailing_title returns the lines to REMOVE.
                    # Actually better to return the split.
                    current_lines = visited_lines

                if subtitle_lines:
                    # Formatted subtitle
                    joined_sub = " ".join([s.strip() for s in subtitle_lines])
                    # Remove outer Parens if desired? User said "paranthetical phrase... is the title".
                    # Maybe keep them or remove them? The user said "insert it". 
                    # Let's keep the parens as they are part of the text, but maybe indent.
                    next_subtitle = f"\n    {joined_sub}\n\n"

            if current_lines:
                chapters.append((current_title, current_lines))
            
            num_str = match.group(1).upper()
            if num_str == "ILI": num_str = "III"
            
            current_title = f"cap_{num_str}"
            current_lines = [line]
            if next_subtitle:
                current_lines.append(next_subtitle)
        else:
            current_lines.append(line)
            
    if current_lines:
        chapters.append((current_title, current_lines))
        
    for idx, (title, ch_lines) in enumerate(chapters):
        safe_title = title.replace(".", "").strip()
        
        if title == "000_toc":
            out_name = "000_toc"
        elif title.startswith("000_"): # dedication
            out_name = "001_dedication" 
        else:
            # Shift index for chapters using a counter or just ensure sorting
            # ded is 001. So cap I should be 001_cap_I if ded is 000? 
            # Current logic: idx 0=TOC, idx 1=Dedication. idx 2=Cap I/II.
            # So naming with idx is safe.
            out_name = f"{idx:03d}_{safe_title}"
            
        (output_dir / f"{out_name}.txt").write_text("".join(ch_lines), encoding="utf-8")

def extract_trailing_title(lines: List[str]):
    """
    Looks for a parenthetical block at the end of lines.
    Returns (subtitle_lines, remaining_lines).
    Subtitle lines include the parentheses.
    """
    if not lines:
        return None, lines
        
    # Scan backwards for non-empty
    end_idx = len(lines) - 1
    while end_idx >= 0 and not lines[end_idx].strip():
        end_idx -= 1
        
    if end_idx < 0:
        return None, lines
        
    # Check if last non-empty line ends with )
    # Check if last non-empty line ends with ) or ).
    stripped_end = lines[end_idx].strip()
    if not (stripped_end.endswith(")") or stripped_end.endswith(").")):
        return None, lines
        
    # Scan backwards for start (
    start_idx = end_idx
    # We allow multi-line titles. Look for the start '('.
    # Brute force back a few lines (max 10?)
    found_start = False
    
    # We strictly look for a line starting with ( or containing it?
    # The examples show: (De quelle ...
    # So valid lines for title are those between ( and ).
    
    # Let's verify identifying the start line.
    for i in range(end_idx, max(-1, end_idx - 10), -1):
        stripped = lines[i].strip()
        if stripped.startswith("("):
            start_idx = i
            found_start = True
            break
            
    if found_start:
        # Check if the structure looks like a single parenthetical block from start_idx to end_idx
        # We assume yes.
        # Subtitle found. Remove the outer parentheses.
        # usually it is (Subtitle...)
        # We start at start_idx and end at end_idx.
        # We can strip the first char from lines[start_idx] and last from lines[end_idx]
        
        # Handle start
        first_line = lines[start_idx].strip()
        if first_line.startswith("("):
            lines[start_idx] = lines[start_idx].replace("(", " ", 1) # Replace first occurence only
            
        # Handle end
        last_line = lines[end_idx].strip()
        if last_line.endswith(")"):
             # We want to replace the LAST ) textually. 
             # Be careful not to replace internal ) if multiple.
             # rsplit might offer a way, or just slicing.
             # But lines[end_idx] might have trailing whitespace.
             val = lines[end_idx].rstrip()
             if val.endswith(")"):
                 val = val[:-1]
                 lines[end_idx] = val + "\n" # restore newline if needed, but lines usually have it? 
                 # Wait, readlines() keeps \n. My clean_lines strips headers but logic in `extract_trailing_title` uses lines list.
                 # If `clean_lines` usage: it returns list of strings.
                 # Let's check `clean_lines`.
        
        subtitle = lines[start_idx : end_idx + 1]
        remaining = lines[:start_idx] + lines[end_idx+1:] # lines[end_idx+1:] are the trailing empty lines
        return subtitle, remaining
        
    return None, lines



if __name__ == "__main__":
    parse_winterberg()
