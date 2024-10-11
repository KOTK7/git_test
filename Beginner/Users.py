class Users:
    def __init__(self, first_name, last_name, age, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.username = username

    def describe_user(self):  # Fixed the method name
        print(f"Hi, my name is {self.first_name} {self.last_name}, "
            f"I'm {self.age} years old, I would like to choose "
            f"{self.username} as my username.")  # Fixed the formatting and string concatenation

    def greet_user(self):
        print(f"Hello {self.username}!")

user1 = Users("Jack", "John", 30, "JackJohn30")
user1.describe_user()  # Call the method
user1.greet_user()  # Call the method

user2 = Users("Jerry", "Tom", 26, "JerryTom26")
user2.describe_user()  # Call the method
user2.greet_user()  # Call the method
