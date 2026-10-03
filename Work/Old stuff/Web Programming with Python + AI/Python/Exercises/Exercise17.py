month = int(input("Enter a month in number format: "))

days31 = (1,3,5,7,8,10,12)
days30 = (4,6,9,11)

if month in days31:
    print("The month you have selected has 31 days.")
if month in days30:
    print("The month you have selected has 30 days.")
if month == 2:
    print("The month you have selected has 28 or 29 days.")