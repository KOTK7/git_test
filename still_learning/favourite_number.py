from pathlib import Path
import json
path = Path("still_learning/number.json")
if path.exists():
    content = path.read_text()
    favourite_number = json.loads(content)
    print(f"your favourite number is: {favourite_number}")
else:
    favourite_number = int(input("input your favourite number"))
    content = json.dumps(favourite_number)
    path.write_text(content)
    print(f"we will remember your favourite number next time: {favourite_number}")