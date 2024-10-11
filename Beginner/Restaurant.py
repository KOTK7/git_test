class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
            print(self.restaurant_name, self.cuisine_type)
    def open_restaurant(self):
        open = f"The {self.restaurant_name} is open!"
        print(open) 
restaurant = Restaurant("Pizza Hut", "Italian")
restaurant.open_restaurant()
restaurant.describe_restaurant()