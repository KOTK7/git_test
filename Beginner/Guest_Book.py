from pathlib import Path

active = True
guest_book = []

while active:
    Name = input("If you want to quit enter q. \nEnter your name please:\n")
    if Name == "q":
        break
    else:
        guest_book.append(Name)

path = Path("guest_book.txt")

# Join the list into a single string with newline characters
content = "\n".join(guest_book)  # Correctly formats the list for writing
path.write_text(content)  # Now this works correctly
print(guest_book)
