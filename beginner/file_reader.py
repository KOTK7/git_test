from pathlib import Path
path = Path("beginner/pi_digits.txt")
contents = path.read_text()
print(contents)