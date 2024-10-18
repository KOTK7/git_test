from pathlib import Path
Name = str(input("Enter your name please: "))
path = Path("Name.txt")
content = path.write_text(Name)