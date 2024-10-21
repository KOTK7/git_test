from employee import Employee
def test_give_raise():
    employee = Employee("John","Jack", 50000)
    employee.give_raise()
    assert employee.annual_salary == 55000
    
def test_give_custom_raise():
    employee = Employee("Jake","Paul", 60000)
    employee.give_raise(3000)
    assert employee.annual_salary == 63000