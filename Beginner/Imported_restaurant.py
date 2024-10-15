from Restaurant import *

# Creating restaurant instances and calling methods
restaurant1 = Restaurant("Pizza Hut", "Italian")
restaurant1.open_restaurant()
restaurant1.describe_restaurant()
restaurant1.update_number_served(30)
restaurant1.increment_number_served(100)

# Calculate total served with additional customers
total_served = restaurant1.total_with_updates(50)  # For example, 50 more customers
print(f"Total customers served at {restaurant1.restaurant_name} (including updates): {total_served}")