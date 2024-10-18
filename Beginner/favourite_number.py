from pathlib import Path
import json
def favourite_num():
    if Path("Fav_num.json"):
        path = Path("Fav_num.json")
        content = path.read_text()
        fav_num = json.loads(content)
        print(f"your favourtie number is: {fav_num}")

    else:
        num = int(input("Enter your favourite number: "))
        path = Path("Fav_num.json")
        content = json.dumps(num)
        path.write_text(content)
favourite_num()