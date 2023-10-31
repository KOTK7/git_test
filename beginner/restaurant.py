class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    def describe_restaurant(self):
        print(f"our restaurant name is: {self.name}, and our cuisine is: {self.cuisine}")
    def open_restaurant(self):
        print(f"our restaurant is open!")
restaurant = Restaurant("cuisiny", "Egyptian")
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavours = ["vanilla","chocolate","peanut butter","mint chocolate"]
    def PrintFlavours(self):
        print(f"our flavours are: {self.flavours}")
ice_cream_stand = IceCreamStand("IceCreamy","global")
ice_cream_stand.PrintFlavours()