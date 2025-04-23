num1 = input('Please enter your first number: ')
# done = input('enter q if done: ')
num2 = input('Please enter your second number: ')

try :
    result = int(num1) + int(num2)
except ValueError:
    print("Please enter numbers not letters")
else:
    print(result)