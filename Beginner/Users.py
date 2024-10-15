class Users:
    def __init__(self, first_name, last_name, age, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        print(f"Hi, my name is {self.first_name} {self.last_name}, "
            f"I'm {self.age} years old, I would like to choose "
            f"{self.username} as my username.")

    def greet_user(self):
        print(f"Hello {self.username}!")

    def increment_login_attempts(self):
        self.login_attempts +=1  # Always increment by the provided number (default is 1)
        print(f"Login attempts for {self.username}: {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login attempts for {self.username} have been reset.")
class Admin(Users):
    def __init__(self, first_name, last_name, age, username):
        super().__init__(first_name, last_name, age, username)
        self.priviliges = ["can ban user", "can add post"," can delete post"]
    def show_privilges(self):
        print(f"Admin can do: {", ".join(self.priviliges)}")
"""
# Create user1
user1 = Users("Jack", "John", 30, "JackJohn30")
user1.describe_user()
user1.greet_user()

# Increment login attempts for user1 multiple times
user1.increment_login_attempts()  # Increment by 1
user1.increment_login_attempts()  # Increment by 1
user1.increment_login_attempts()  # Increment by 1

# Reset login attempts for user1
user1.reset_login_attempts()

# Create user2
user2 = Users("Jerry", "Tom", 26, "JerryTom26")
user2.describe_user()
user2.greet_user()

# Increment login attempts for user2 multiple times
user2.increment_login_attempts()  # Increment by 1
user2.increment_login_attempts()  # Increment by 1

# Reset login attempts for user2
user2.reset_login_attempts()
"""
IamAdmin = Admin("Zeko","Paul",24,"zekopaul24")
IamAdmin.show_privilges()