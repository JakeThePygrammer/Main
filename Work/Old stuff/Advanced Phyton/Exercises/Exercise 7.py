class Store:
    def __init__(self, name, employees, profit):
        self.name = name
        self.employees = employees
        self.profit = profit
    def __str__(self):
        return f"Name {self.name}, Employees {self.employees}, Profit {self.profit}"
class ClothingStore(Store):
    def __init__(self, name, employees, profit, changing_rooms, season):
        super().__init__(name,employees,profit)
        self.changing_rooms = changing_rooms
        self.season = season
    def __str__(self):
        return f"Name {self.name}, Employees {self.employees}, Profit {self.profit}, Changing rooms {self.changing_rooms}, Season {self.season}."
class FoodStore(Store):
    def __init__(self, name, employees, profit, food_type, total_working_days):
        super().__init__(name,employees,profit)
        self.food_type = food_type
        self.total_working_days = total_working_days
    def __str__(self):
        return f"Name {self.name}, Employees {self.employees}, Profit {self.profit}, Food type {self.food_type}, Total working days {self.total_working_days}."
    def averagedailyincome(self):
        averageincome = int(self.profit) / int(self.total_working_days)
        return averageincome

store1 = Store("Tinex", "18", "175000")
store2 = Store("Trimaks", "3", "150000")
clothingstore1 = ClothingStore("Koton", "10", "230000", "8", "Fall 2024")
clothingstore2 = ClothingStore("LC Waikiki", "15", "95000", "20", "Fall 2024")
foodstore1 = FoodStore("KFC", "10", "120000", "Chicken", "260")
foodstore2 = FoodStore("Burger king", "15", "150000", "Burger", "245")

print(store1)
print(store2)
print(clothingstore1)
print(clothingstore2)
print(foodstore1)
print(foodstore2)

print(foodstore1.averagedailyincome())
print(foodstore2.averagedailyincome())