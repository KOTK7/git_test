def addition():
    try:
        a = int(input("number 1: "))
        b = int(input("number 2: "))
        result = a+b
    except ValueError:
        print("input a number please")
    else:
        print(result)
addition()