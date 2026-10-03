class Product:
    def __init__(self, name, serial_number, price, type, amount = 0):
        self.name = name
        self.serial_number = serial_number
        self.price = price
        self.type = type
        self.amount = amount
    def __str__(self):
        return f"{self.name}, {self.serial_number}, {self.price}, {self.type}, {self.amount}"

class Shop:
    def __init__(self, name, serial_number, products = []):
        self.name = name
        self.serial_number = serial_number
        self.products = products
    def add_product(self, product):
        if type(product) == Product:
            self.products.append(product)
    def allprices(self):
        prices = 0
        for item in self.products:
            prices += item.price
        print(prices)
    def __str__(self):
        a = []
        for item in self.products:
            a.append(item.name)
        return f"Shop name : {self.name}, s/n : {self.serial_number}, Products : {a}"

shop = Shop("Bakery", 1)
a = Product("Burek 1/8", 13145, 120, "Baked goods")
b = Product("Burek 1/4", 13146, 170, "Baked goods")
shop.add_product(a)
shop.add_product(b)
print(shop)
shop.allprices()

