class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
    
    def describe_restaurant(self):
        print(f"The restaurant name is {self.name} and its cuisine is {self.cuisine}\n")

    def open_restaurant(self):
        print('the restaurant is open')

restaurant1 = Restaurant('Mariano', 'Italian')

restaurant1.describe_restaurant()

restaurant1.open_restaurant()