class Employee:
    def __init__(self, first_name, last_name, annual_salary=70000):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, added_salary=0):
        self.annual_salary += added_salary
        return f"{self.first_name} {self.last_name} {self.annual_salary}$"

    def get_info(self):
        return f"{self.first_name} {self.last_name} {self.annual_salary}$"

    def show_info(self):
        print(self.get_info())

employee = Employee('Jack',"Paul")
employee.give_raise(6000)
employee.show_info()