print("Give two numbers and I will add them")
print("Enter q to exit")
active = True
while active:
    first_number = input("Please enter the first number: ")
    if first_number == "q":
        break
    second_number = input("Please enter the second number: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Enter a number please.")
    else:
        print(answer)