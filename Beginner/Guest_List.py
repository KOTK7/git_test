guest_list = ["John Medhat","Mohamed Mostafa","Mahmoud Naser"]
print(f"Hello {guest_list[0]}, Would you like to come for dinner tonight?")
print(f"Hello {guest_list[1]}, Would you like to come for dinner tonight?")
print(f"Hello {guest_list[2]}, Would you like to come for dinner tonight?")

print(f"{guest_list[2]}, Can't attend tonight's dinner")
guest_list[2] = "Rabee"

print(f"Hello {guest_list[0]}, Would you like to come for dinner tonight?")
print(f"Hello {guest_list[1]}, Would you like to come for dinner tonight?")
print(f"Hello {guest_list[2]}, Would you like to come for dinner tonight?")
print("Great news! I found a bigger table")

guest_list.insert(0, "Mohamed Osama")
guest_list.insert(2, "Gamal Ashraf")
guest_list.insert(3, "Hatem Hazem")

print(f"Hello {guest_list[0]}, Would you like to come for dinner tonight?")
print(f"Hello {guest_list[1]}, Would you like to come for dinner tonight?")
print(f"Hello {guest_list[2]}, Would you like to come for dinner tonight?")
print(f"Hello {guest_list[3]}, Would you like to come for dinner tonight?")
print(f"Hello {guest_list[4]}, Would you like to come for dinner tonight?")
print(f"Hello {guest_list[5]}, Would you like to come for dinner tonight?")
print("I'm sorry but i can't invite more than two")

popped_guests =[guest_list.pop(0), guest_list.pop(0),guest_list.pop(0),guest_list.pop(0)]
for guest in popped_guests:
    print(f"I'm so sorry {guest}, I can only invite two people")

for bozo in guest_list:
    print(f"You are still invited {bozo}")

del guest_list[0]
del guest_list[0]
print(guest_list)
#** That was a lot of work, phew!