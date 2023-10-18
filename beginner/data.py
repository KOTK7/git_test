data = {}
user_email = input("enter your email please : ")
user_name = input("enter your user name please : ")
data["email"] = user_email
data["user name"] = user_name
print(f"Welcome {user_name}!, your email is {user_email}. \n")
print("is it correct?")
boolean = (input())
if boolean == "yes":
    print("awesome")
else:
    print("please try again")
for i in data:
    print(data.get(i))