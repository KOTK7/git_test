from pathlib import Path

path= Path("learning_python.txt") 
content = path.read_text()
P_learn = []
lines = content.splitlines()
for line in lines:
    P_learn += line
print("".join(P_learn))
print(content)
replace = content.replace("python", "C")
print(replace)