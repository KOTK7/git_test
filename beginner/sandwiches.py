sandwiches = ["pastarmi","tuna","ham"]
finished_sandwiches = []
while sandwiches:
    user_sandwich = sandwiches.pop()
    print(f"i made your {user_sandwich} sandwich")
    finished_sandwiches.append(user_sandwich)
    
print(finished_sandwiches)
