class Shopper:
    def __init__(self,name,surname,money):
        self.name = name
        self.surname = surname
        self.money = money
    def __str__(self):
        return f"Name: {self.name} Surname: {self.surname} Money: {self.money} "
    def lowerMoney(self,value):
        if self.money - value >= 0:
            self.money -= value
        else:
            self.money = 0
s1 = Shopper("Jake", "Nestor", 1000)
s2 = Shopper("Ana", "Colland", 800)
s3 = Shopper("Marko", "Simonov", 600)
list_shoppers = [s1,s2,s3]
max_money = 0
money_combined = 0
for index in list_shoppers:
    money_combined += index.money
    if index.money > max_money:
        max_money = index.money
        max_money_shopper = index
print(max_money_shopper)
print(f"Everyone combined has {money_combined} dollars.")
