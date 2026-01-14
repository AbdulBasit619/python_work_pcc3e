"""Get stored username if available"""

from pathlib import Path
import json

path = Path("favourite_number.txt")
if path.exists():
    contents = path.read_text()
    favourite_number = json.loads(contents)
    print(f"I know your favourite number! It's {favourite_number}")
else:
    print(f"The file {path} does not exist!")
