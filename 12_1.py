class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, initial_rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = initial_rating

    def describe_restaurant(self):
        description = "Restaurant: " + self.restaurant_name + "\nCuisine type: " + self.cuisine_type + "\nRating: " + str(self.rating)
        return description

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, initial_rating, flavors):
        super().__init__(restaurant_name, cuisine_type, initial_rating)
        self.flavors = flavors

    def display_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print(flavor)
ice_cream_stand = IceCreamStand("Sweet Treats", "Ice Cream", 4.7, ["Vanilla", "Chocolate", "Strawberry"])
ice_cream_stand.display_flavors()