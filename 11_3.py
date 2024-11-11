class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, initial_rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = initial_rating

    def describe_restaurant(self):
        print("Restaurant Name:", self.restaurant_name)
        print("Cuisine Type:", self.cuisine_type)
        print("Rating:", self.rating)

    def update_rating(self, new_rating):
        self.rating = new_rating

restaurant1 = Restaurant("Tbiliso", "Georgian", 4.5)
restaurant1.update_rating(4.8)
restaurant1.describe_restaurant()