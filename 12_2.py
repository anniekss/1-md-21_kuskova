class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, location, hours ):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.location = location
        self.hours = hours


    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Местоположение:: {self.location}")
        print(f"Время работы: {self.hours}")

    def open_restaurant(self):
        print("Ресторан открыт!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, location, hours):
        super().__init__(restaurant_name, cuisine_type, location, hours)
        self.location = location
        self.hours = hours
        self.flavors = []
        self.ice_cream_types = []

    def add_ice_cream_type(self, ice_cream_type):
        self.ice_cream_types.append(ice_cream_type)

    def remove_ice_cream_type(self, ice_cream_type):
        if ice_cream_type in self.ice_cream_types:
            self.ice_cream_types.remove(ice_cream_type)

    def has_ice_cream_type(self, ice_cream_type):
        return ice_cream_type in self.ice_cream_types

    def describe_ice_cream_types(self):
        print("Типы мороженого:")
        for ice_cream_type in self.ice_cream_types:
            print(f"\t- {ice_cream_type}")

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)

    def has_flavor(self, flavor):
        return flavor in self.flavors

    def describe_location(self):
        print(f"Расположение: {self.location}")

    def display_hours(self):
        print(f"Часы работы: {self.hours}")

    def describe_flavors(self):
        print("Сорта мороженого:")
        for flavor in self.flavors:
            print(f"\t- {flavor}")

newIceCreamStand = IceCreamStand("Сладкоежка", "Мороженое", "проспект Ударников, 32", "10:00 - 20:00")
newIceCreamStand.add_ice_cream_type("Шоколад")
newIceCreamStand.add_ice_cream_type("Ваниль")
newIceCreamStand.add_ice_cream_type("Фисташка")
newIceCreamStand.describe_restaurant()
newIceCreamStand.describe_ice_cream_types()