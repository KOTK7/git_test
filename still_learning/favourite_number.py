from pathlib import Path
import json
Favourite_number = int(input("input your favourite number please: "))
path = Path("number.json")
content = json.dumps(Favourite_number)
path.write_text(content)