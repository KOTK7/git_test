class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print('the dog is sitting')
    
    def roll_over(self):
        print('the dog is rolling over')
    
    def who(self):
        print(f"The dog's name is {self.name}, and he is {self.age} years old.")


dog1 = Dog('Max', '4')

dog1.who()


class Puppy(Dog):
    def __init__(self, name, age):
        super().__init__(name,age)

puppy = Puppy('little max', '1.5')
puppy.who()