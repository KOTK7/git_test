from pathlib import Path

path = Path('learning_python.txt')
content = path.read_text()
replace = content.replace('Python', 'C')
print(replace)