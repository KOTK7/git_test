"""
basic arithmetics
x + y addition
x - y subtraction
x * y multiplication
x / y division
x ** y exponentiation
x % y remainder
x // y how many times does y get into x.
"""
#Examples
x = int(input("first number"))
y = int(input("second number"))
operator = input("what's your operator?")
if operator == "*":
    print(x * y)
elif operator == "+":
    print(x + y)
elif operator == "-":
    print(x - y)
elif operator == "/":
    print(x / y)
elif operator == "//":
    print(x // y)
elif operator == "**":
    print(x ** y)
elif operator == "%":
    print(x % y)