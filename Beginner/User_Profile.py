def build_profile(first, last, **user_info):
    user_info["first name"] = first
    user_info["last name"] = last
    return user_info
user_profile = build_profile("Jack","Johns", Status = "single", Student = "Nope")
print(f"Hi my name is: {user_profile['first name']} {user_profile['last name']}, I'm {user_profile['Status']} and i'm not a Student")