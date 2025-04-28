from Employee import Employee

def test_base_salary_with_names():
    employee = Employee('Jack',"Paul")
    info = employee.get_info()
    assert info == "Jack Paul 70000$"

def test_give_raise():
    employee = Employee('Jack', 'Paul')
    assert employee.give_raise(6000) == 'Jack Paul 76000$'