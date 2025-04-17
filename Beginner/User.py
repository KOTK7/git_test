class User:
    def __init__(self, first_name, last_name, user_name):
        self.f_name = first_name
        self.l_name = last_name
        self.username = user_name

    def describe_user(self):
        print(f"the user's first name is {self.f_name}")
        print(f"and his last name is {self.l_name} and his username is {self.username}")
    
    def greet_user(self):
        print(f"Hello {self.username}, it is nice to see you back!")

user1 = User('Jack','Paul','jakey22')
user1.describe_user()
user1.greet_user()