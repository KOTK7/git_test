from pathlib import Path
import json
path = Path("still_learning/number.json")
content = path.read_text()
numbers = json.loads(content)
print(numbers)