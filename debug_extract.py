
def extract_trailing_title(lines):
    # Strip empty lines from end? No, just ignore them.
    # We want to find the last block ( ... )
    
    end_idx = len(lines) - 1
    while end_idx >= 0 and not lines[end_idx].strip():
        end_idx -= 1
        
    if end_idx < 0:
        return None, lines
        
    # Check if last non-empty line ends with )
    print(f"Checking line {end_idx}: '{lines[end_idx].strip()}'")
    if not lines[end_idx].strip().endswith(")"):
        print("Does not end with )")
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
        print(f"Scanning line {i}: '{stripped}'")
        if stripped.startswith("("):
            start_idx = i
            found_start = True
            break
            
    if found_start:
        # Check if the structure looks like a single parenthetical block from start_idx to end_idx
        # We assume yes.
        subtitle = lines[start_idx : end_idx + 1]
        remaining = lines[:start_idx] + lines[end_idx+1:] # lines[end_idx+1:] are the trailing empty lines
        return subtitle, remaining
        
    print("Start ( not found")
    return None, lines

lines = [
    "Test content line 1.",
    "Test content line 2.",
    "",
    "(De fabrica seu formatione eorum 5 regularium et deproportione",
    "cujusque ad diametruni spere et primo de tetracedron).",
    "",
    ""
]

sub, rem = extract_trailing_title(lines)
print("\nResult:")
if sub:
    print("Subtitle found:")
    print(sub)
else:
    print("No subtitle found.")
