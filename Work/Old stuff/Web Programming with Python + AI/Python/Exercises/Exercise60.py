class Product:
    def __init__(self, name, serial_number, price, type, amount = 0):
        self.name = name
        self.serial_number = serial_number
        self.price = price
        self.type = type
        self.amount = amount
    def __str__(self):
        return f"{self.name}, {self.serial_number}, {self.price}, {self.type}, {self.amount}"

a = Product("Burek 1/8", 13145, 120, "Baked goods")
print(a)
print(type(a))
