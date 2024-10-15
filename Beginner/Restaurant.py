class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Initialize the number served

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)

    def open_restaurant(self):
        open_message = f"The {self.restaurant_name} is open!"
        print(open_message)

    def update_number_served(self, served):
        self.number_served = served
        print(f"Total number of customers served: {served}")

    def increment_number_served(self, served):
        self.number_served += served
        print(f"We have served an additional {served} customers today!")

    def total_served(self):
        return self.number_served

    def total_with_updates(self, additional_served):
        total = self.number_served + additional_served
        return total
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ["Chocolate", "Vanilla", "Mint Chocolate"]

    def Flavours(self):
        print(f"We have: {', '.join(self.flavours)}. What would you like to have?")
"""
# Creating restaurant instances and calling methods
restaurant1 = Restaurant("Pizza Hut", "Italian")
restaurant1.open_restaurant()
restaurant1.describe_restaurant()
restaurant1.update_number_served(30)
restaurant1.increment_number_served(100)

# Calculate total served with additional customers
total_served = restaurant1.total_with_updates(50)  # For example, 50 more customers
print(f"Total customers served at {restaurant1.restaurant_name} (including updates): {total_served}")

restaurant2 = Restaurant("Masrawy", "Egyptian")
restaurant2.open_restaurant()
restaurant2.describe_restaurant()
restaurant2.update_number_served(30)
restaurant2.increment_number_served(100)

# Calculate total served with additional customers
total_served = restaurant2.total_with_updates(20)  # For example, 20 more customers
print(f"Total customers served at {restaurant2.restaurant_name} (including updates): {total_served}")

restaurant3 = Restaurant("Hooters", "American")
restaurant3.open_restaurant()
restaurant3.describe_restaurant()
restaurant3.update_number_served(30)
restaurant3.increment_number_served(100)

# Calculate total served with additional customers
total_served = restaurant3.total_with_updates(10)  # For example, 10 more customers
print(f"Total customers served at {restaurant3.restaurant_name} (including updates): {total_served}")
"""
# Creating an instance of IceCreamStand
IwantIceCream = IceCreamStand("My Ice Cream Stand", "Ice Cream")
IwantIceCream.Flavours()