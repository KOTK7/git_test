data = {}
data["email"] = input("enter your email please : ")
data["user name"] = input("enter your user name please : ")
print(f"Welcome {data['user name']}!, your email is {data['email']}. \n")
print("is it correct?")
boolean = (input())
if boolean == "yes":
    print("awesome!")
else:
    print("please try again")