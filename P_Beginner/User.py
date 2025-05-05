class User:
    def __init__(self, first_name, last_name, user_name):
        self.f_name = first_name
        self.l_name = last_name
        self.username = user_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user's first name is {self.f_name}")
        print(f"And their last name is {self.l_name} and their username is {self.username}")
    
    def greet_user(self):
        print(f"Hello {self.username}, it is nice to see you back!")

    def increment_login_attempts(self, no_of_logins=1):
        self.login_attempts += no_of_logins
        print(f"{no_of_logins} login attempt(s) added. Total login attempts now: {self.login_attempts}")

    def show_attempts(self):
        print(f"{self.username}'s login attempts: {self.login_attempts}")

    def reset_login_attempts(self):
        print(f"Resetting login attempts for {self.username}. Previous attempts: {self.login_attempts}")
        self.login_attempts = 0

user1 = User('Jack', 'Paul', "Jackey22")

user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.show_attempts()
user1.reset_login_attempts()