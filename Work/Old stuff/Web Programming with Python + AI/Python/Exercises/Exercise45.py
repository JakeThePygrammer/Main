lowerprice = lambda price, lowerpercent: price - price //100 * lowerpercent

a = int(input("Enter price: "))
b = int(input("Enter discount: "))

print(f"Lowered price: {lowerprice(a, b)}")
