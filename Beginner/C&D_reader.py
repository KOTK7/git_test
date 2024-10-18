from pathlib import Path
try:
    path1 = Path("Cats.txt")
    path2 = Path("Dogs.txt")
    content1 = path1.read_text()
    content2 = path2.read_text()
except FileNotFoundError:
    pass
else:
    print(content1)
    print(content2)