from __future__ import annotations
from pathlib import Path
from geometor.pacioli.parser import PacioliParser

def main():
    resources_dir = Path("/home/phi/PROJECTS/geometor/pacioli/resources/de_divina_proportione")
    output_dir = Path("/home/phi/PROJECTS/geometor/pacioli/docsrc/divina")
    
    parser = PacioliParser(resources_dir, output_dir)
    parser.parse()

if __name__ == "__main__":
    main()
