# Define the Guest class
class Guest:
    def __init__(self, name, meal_preference, table_number):
        self.name = name
        self.meal_preference = meal_preference
        self.table_number = table_number

    def show_info(self):
        print(f"Hello Mr. {self.name}, your favorite meal is {self.meal_preference} and your table number is {self.table_number}.")

# Create a list of Guest objects
guests_list = [
    Guest("Louis", "Fish", 7),
    Guest("Mike", "Pizza", 5),
    Guest("Harvey", "Steak", 6)
]

# Send invitations using the list
def send_invitation():
    for guest in guests_list:
        print(f"Dear Mr. {guest.name}, we are delighted to invite you to our event!")

# Call the function to send invitations
send_invitation()

# Show guest info
for guest in guests_list:
    guest.show_info()
