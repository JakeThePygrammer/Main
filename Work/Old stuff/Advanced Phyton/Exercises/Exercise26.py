class Store:
    def __init__(self, store_name, number_of_workers, address):
        self.store_name = store_name
        self.number_of_workers = number_of_workers
        self.address = address
    def __str__(self):
        return f"Store name : {self.store_name}, number of workers : {self.number_of_workers}, address : {self.address}."
s1 = Store("Zara", "20", "Blvd. Partizanski Odredi br. 21")

class ClothingStore(Store):
    def __init__(self, store_name, number_of_workers, address, brands = {}):
        super().__init__(store_name, number_of_workers, address)
        self.brands = brands
    def __str__(self):
        return f"Store name : {self.store_name}, number of workers : {self.number_of_workers}, address : {self.address}, brands : {self.brands.keys()}."
    def brandsandrating(self):
        for k,v in self.brands.items():
            print(f"Brand : {k} ---------> Rating : {v}")
    def highestrating(self):
        max_rating = 0.0
        highest_rated = None
        for k,v in self.brands.items():
            if float(v) > max_rating:
                max_rating = float(v)
                highest_rated = f"{k} is the highest rated, with a rating of {v}"
        return highest_rated
s2 = ClothingStore("Zara", "20", "Blvd. Partizanski Odredi br. 21",{"Vershache" : 3.5, "Levi's" : 4.3, "Prada" : 4.6})
print(s2)
s2.brandsandrating()
print(s2.highestrating())
