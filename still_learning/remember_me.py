from pathlib import Path
import json
user_data = {}
user_data["username"] = input("What is your name?: ")
user_data["userage"] = int(input("what is your age?: "))
user_data["usersex"] = input("what is your sex?: ")
path = Path('username.json')
contents = json.dumps(user_data)
path.write_text(contents)
print(f"We'll remember you when you come back, {user_data}!")