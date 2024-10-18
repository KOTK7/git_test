from pathlib import Path

active = True
guest_book = []

while active:
    q = input("Enter q to exit or if you want to add someone else's name just enter any key: ")
    if q == "q":
        break
    else:
        Name = input("Enter your name please: ")
        guest_book.append(Name)

path = Path("guest_book.txt")

# Join the list into a single string with newline characters
content = "\n".join(guest_book)  # Correctly formats the list for writing
path.write_text(content)  # Now this works correctly
print(guest_book)
