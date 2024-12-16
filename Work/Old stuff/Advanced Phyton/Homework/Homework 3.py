class Business:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Name : {self.name}"

class Store(Business):
    def __init__(self, location, name):
        super().__init__(name)
        self.location = location

    def __str__(self):
        return f"Name : {self.name}, Location : {self.location}"

class Restaurant(Business):
    def __init__(self, cuisine, num_tables, name):
        super().__init__(name)
        self.cuisine = cuisine
        self.num_tables = num_tables

    def __str__(self):
        return f"Name : {self.name}, Cuisine : {self.cuisine}, Tables : {self.num_tables}"

class ClothingStore(Store):
    def __init__(self, clothing_type, num_wardrobes, location, name):
        super().__init__(location, name)
        self.clothing_type = clothing_type
        self.num_wardrobes = num_wardrobes

    def __str__(self):
        return (f"Name : {self.name}, Location : {self.location}, "
                f"Clothing type : {self.clothing_type}, Wardrobes : {self.num_wardrobes}")

class FoodStore(Store):
    def __init__(self, food_category, location, name):
        super().__init__(location, name)
        self.food_category = food_category

    def __str__(self):
        return (f"Name : {self.name}, Location : {self.location}, "
                f"Food category : {self.food_category}")

# Creating Restaurant Instances
r1 = Restaurant("Mexican", 15, "Buenos Dias")
r2 = Restaurant("Chinese", 20, "Star Ocean")
r3 = Restaurant("Balkan", 10, "Merak Meana")
restaurant_list = [r1, r2, r3]

# Creating ClothingStore Instances
c1 = ClothingStore("Casual", 10, "Kapitol mall", "LC Waikiki")
c2 = ClothingStore("Business-casual", 8, "Kapitol mall", "Koton")
c3 = ClothingStore("Leisurewear", 25, "City mall", "Zara")
clothing_list = [c1, c2, c3]


max_tables = 0
max_table_restaurant = None

for restaurant in restaurant_list:
    if restaurant.num_tables > max_tables:
        max_tables = restaurant.num_tables
        max_table_restaurant = restaurant

print(f"The restaurant with the most tables is: {max_table_restaurant.name}")

max_wardrobes = 0
max_wardrobes_store = None

for store in clothing_list:
    if store.num_wardrobes > max_wardrobes:
        max_wardrobes = store.num_wardrobes
        max_wardrobes_store = store

print(f"The clothing store with the most wardrobes is: {max_wardrobes_store.name}")
