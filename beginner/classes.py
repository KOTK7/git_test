class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age= age
    def sit(self):
        print(f"{self.name} is sitting")
    def roll_over(self):
        print(f"{self.name} rolled over")
my_dog = Dog("willie",6)
print(f"my dog's name is {my_dog.name}")
print(f"my dog's is {my_dog.age} years old")