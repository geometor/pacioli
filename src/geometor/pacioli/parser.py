import re
from pathlib import Path
from typing import List, Dict, Optional

class PacioliParser:
    def __init__(self, resources_dir: Path, output_dir: Path):
        self.resources_dir = resources_dir
        self.output_dir = output_dir
        self.transcribed_file = resources_dir / "gri-ark--13960-t48p7rw0p-1680998311.txt"

    def parse(self):
        """Main execution method."""
        print(f"Parsing resources from: {self.resources_dir}")
        print(f"Outputting to: {self.output_dir}")
        
        if not self.transcribed_file.exists():
            print(f"Error: Transcribed file not found at {self.transcribed_file}")
            return

        content = self.transcribed_file.read_text(encoding='utf-8')
        lines = content.splitlines()

        # Define Books (Ranges are approximate based on analysis, can be refined)
        # Book 1: Divina Proportione
        # TOC: ~1170 - ~1540
        # Text: ~1615 - ~5600
        
        # Book 2: Architectura
        # TOC: ~1540 - ~1600
        # Text: ~5614 - ~7380
        
        # We will extract these sections based on markers
        
        books = [
            {
                "name": "proportione",
                "toc_start_marker": "Cap. I. Epistola a lo excellentissimo",
                "text_start_marker": "Excellentissimo principi Ludouico mariae Sforza", # Start of text (no header)
                "text_end_marker": "(Dela mesura e proportioni del corpo humano", # End of text (Start of Arch)
                "gap_start_marker": "Gap. II." # Gap I is missing header, special handling
            },
            {
                "name": "architectura",
                "toc_start_marker": "Tabula del tractato de larchitectura",
                "text_start_marker": "Gap. I.",
                "text_end_marker": "Gap. I. Rühmende Erwähnung" # Start of German
            }
        ]

        for book in books:
            self.process_book(lines, book)

        # Generate root index.rst
        self.create_root_index([b['name'] for b in books])

    def create_root_index(self, book_names: List[str]):
        index_content = """
:navigation: header

De Divina Proportione
=====================

.. toctree::
   :maxdepth: 2
   :caption: Books

"""
        for name in book_names:
            index_content += f"   {name}/index\n"

        (self.output_dir / "index.rst").write_text(index_content, encoding='utf-8')

    def process_book(self, lines: List[str], book_config: Dict):
        print(f"Processing book: {book_config['name']}")
        
        # 1. Extract TOC Chapters (Titles)
        toc_chapters = self.extract_chapters(lines, book_config['toc_start_marker'], book_config.get('text_start_marker'), "Cap")
        print(f"  Found {len(toc_chapters)} TOC chapters.")
        
        # 2. Extract Text Chapters (Content)
        # Note: Text extraction needs to handle the start/end markers carefully
        text_chapters = self.extract_chapters(lines, book_config['text_start_marker'], book_config.get('text_end_marker'), "Gap")
        print(f"  Found {len(text_chapters)} Text chapters.")
        
        # Special handling for Proportione Book 1 Chapter 1 (Missing Gap. I.)
        if book_config['name'] == 'proportione':
            # We need to manually create Chapter 1 text from the start marker up to Gap. II.
            # Or just rely on the fact that extract_chapters might miss it if it looks for "Gap."
            # Let's see if we can capture it.
            pass

        # 3. Merge Chapters
        merged_chapters = self.merge_chapters(toc_chapters, text_chapters)
        print(f"  Merged into {len(merged_chapters)} chapters.")

        # 4. Generate RST
        book_output_dir = self.output_dir / book_config['name']
        self.generate_rst_structure(merged_chapters, book_output_dir)

    def extract_chapters(self, lines: List[str], start_marker: str, end_marker: str, prefix: str) -> Dict[str, Dict]:
        """
        Extracts chapters from a section of lines.
        Returns a dict keyed by Roman Numeral ID.
        """
        chapters = {}
        in_section = False
        current_chapter = None
        buffer = []
        
        # Regex for "Cap. X." or "Gap. X."
        # Note: Gap. I. might be missing in some places
        pattern = re.compile(r"^\s*" + prefix + r"\.\s+([IVXLCDM]+)\.", re.IGNORECASE)
        
        start_idx = -1
        end_idx = len(lines)
        
        # Find start/end indices
        for i, line in enumerate(lines):
            if start_marker in line:
                start_idx = i
                break
        
        if start_idx == -1:
            print(f"  Warning: Start marker '{start_marker}' not found.")
            return {}

        if end_marker:
            for i in range(start_idx + 1, len(lines)):
                if end_marker in lines[i]: # Changed 'line' to 'lines[i]'
                    end_idx = i
                    break
        
        print(f"  Scanning lines {start_idx} to {end_idx} for '{prefix}'...")

        # Special case for Proportione Text Chapter 1 (starts at start_marker without "Gap. I.")
        if prefix == "Gap" and "Excellentissimo" in start_marker:
             current_chapter = {
                "id": "I",
                "title": "", # Title comes from TOC
                "content": ""
            }
             # We start capturing immediately
             in_section = True

        for i in range(start_idx, end_idx):
            line = lines[i]
            match = pattern.match(line)
            
            if match:
                # Save previous chapter
                if current_chapter:
                    current_chapter['content'] = "\n".join(buffer).strip()
                    chapters[current_chapter['id']] = current_chapter
                
                # Start new chapter
                roman_num = match.group(1).upper()
                current_chapter = {
                    "id": roman_num,
                    "title": line.strip(), # This might be the title (TOC) or just "Gap. X." (Text)
                    "content": ""
                }
                buffer = []
                in_section = True
            elif in_section:
                buffer.append(line)
        
        # Save last chapter
        if current_chapter:
            current_chapter['content'] = "\n".join(buffer).strip()
            chapters[current_chapter['id']] = current_chapter
            
        return chapters

    def merge_chapters(self, toc_chapters: Dict, text_chapters: Dict) -> List[Dict]:
        """
        Merges TOC and Text chapters.
        """
        merged = []
        all_ids = set(toc_chapters.keys()) | set(text_chapters.keys())
        
        def roman_to_int(s):
            rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            int_val = 0
            for i in range(len(s)):
                if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                    int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
                else:
                    int_val += rom_val[s[i]]
            return int_val

        sorted_ids = sorted(list(all_ids), key=roman_to_int)
        
        for i, chapter_id in enumerate(sorted_ids):
            toc = toc_chapters.get(chapter_id, {})
            text = text_chapters.get(chapter_id, {})
            
            # Title comes from TOC, Content from Text
            # If Text is missing, we might have a placeholder
            # If TOC is missing, we use what we have
            
            title = toc.get('title', text.get('title', f"Chapter {chapter_id}"))
            # Clean title: Remove "Cap. X." prefix if present
            title = re.sub(r"^\s*Cap\.\s+[IVXLCDM]+\.\s*", "", title, flags=re.IGNORECASE)
            
            content = text.get('content', "")
            
            merged.append({
                "id": chapter_id,
                "order": i + 1,
                "title": title,
                "content": content
            })
            
        return merged

    def generate_rst_structure(self, chapters: List[Dict], output_dir: Path):
        """
        Generates the RST folder structure and files.
        """
        if not output_dir.exists():
            output_dir.mkdir(parents=True)

        # Create main index.rst
        self.create_main_index(chapters, output_dir)

        for chapter in chapters:
            chapter_id = chapter['id']
            folder_name = f"capitulum_{chapter_id}"
            chapter_dir = output_dir / folder_name
            chapter_dir.mkdir(exist_ok=True)
            
            self.create_chapter_files(chapter_dir, chapter)

    def create_main_index(self, chapters: List[Dict], output_dir: Path):
        index_content = f"""
{output_dir.name.replace('_', ' ').title()}
{'=' * len(output_dir.name)}

.. toctree::
   :maxdepth: 1
   :caption: Chapters

"""
        for chapter in chapters:
            chapter_id = chapter['id']
            index_content += f"   capitulum_{chapter_id}/index\n"

        (output_dir / "index.rst").write_text(index_content, encoding='utf-8')

    def create_chapter_files(self, chapter_dir: Path, chapter: Dict):
        # index.rst
        # Add Anchor and Order
        # Add full text in code block
        
        # Extract first line of content for "text of first line after the chapter heading" ??
        # The user said "include the full text in the code-block (text of first line after the chapter heading)"
        # I assume they mean the *entire* text content of the chapter.
        
        index_content = f"""
:order: {chapter['order']}

.. _capitulum_{chapter['id']}:

{chapter['title']}
{'=' * len(chapter['title'])}

.. include:: english.rst
.. include:: notes.rst

Original Text
-------------

.. code-block:: text

{self.indent_text(chapter['content'])}

"""
        (chapter_dir / "index.rst").write_text(index_content, encoding='utf-8')
        
        # english.rst
        english_content = """
Translation
-----------

.. note::
   English translation to be added.
"""
        (chapter_dir / "english.rst").write_text(english_content, encoding='utf-8')
        
        # notes.rst
        notes_content = """
Notes
-----

.. note::
   Notes to be added.
"""
        (chapter_dir / "notes.rst").write_text(notes_content, encoding='utf-8')

    def indent_text(self, text: str, indent: str = "   ") -> str:
        return "\n".join(indent + line for line in text.splitlines())
