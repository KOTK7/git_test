users = []
if users:
    for user in users:
        if user == "admin":
            print(f"Hello {user}, would you like to see status report?")
        else:
            print(f"Hello {user}, Thank you for logging in again.")
else:
    print("We need to find some users!")