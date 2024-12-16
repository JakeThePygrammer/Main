class Product:
    def __init__(self, naziv, seriski_broj, cena, tip, kolichina=0):
        self.naziv = naziv
        self.seriski_broj = seriski_broj
        self.cena = cena
        self.tip = tip
        self.kolichina = kolichina
    def __str__(self):
        return f"naziv = {self.naziv}, seriski broj = {self.seriski_broj}, cena={self.cena}, tip={self.tip}, kolichina={self.kolichina}"
    def changeStock(self,vrednost):
        if vrednost >= 0:
            self.kolichina = vrednost

#p = Product("laptop","A3213","550","Elektronika",4)
#p.changeStock(12)
#print(p)
#name = input("name")
#serial = input("serial")
#price = input("price")
#type = input("type")
#stock = input("stock")
#p2 = Product(name,serial,price,type,stock)
#print(p2)

p1 = Product(input("name"),input("serial"),int(input("price")),input("type"),input("stock"))
p2 = Product(input("name"),input("serial"),int(input("price")),input("type"),input("stock"))

if p1.cena < p2.cena:
    print(f"{p2.naziv} e poskapo od {p1.naziv}")
elif p1.cena == p2.cena:
    print(f"{p2.naziv} i {p1.naziv} se ednakvi vo cena")
else:
    print(f"{p1.naziv} e poskapo od {p2.naziv}")

p3 = Product(input("name"),input("serial"),int(input("price")),input("type"),input("stock"))

product_list = [p1,p2,p3]
max_cena = 0
for index in product_list:
    if index.cena > max_cena:
        max_cena = index.cena
        max_product = index
print(max_product)


