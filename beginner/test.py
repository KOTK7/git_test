age = int(input())
while True:
    if age < 3:
        print("ticket is free")
    elif age > 3 and age <12:
        print("the ticket is 10$")
    elif age > 12:
        print("the ticket is 15$")
    break
