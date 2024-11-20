class Dog:
    def __init__(self, name, age):
        """Initializing the class"""
        self.name = name
        self.age = age
    
    def sit(self):
        """a function for the dog to sit"""
        print(f"{self.name} is sitting")

    def roll_over(self):
        """a function for the dog to roll over"""
        print(f"{self.name} is rolling over")
my_dog = Dog("Max",9)
print(my_dog.age)