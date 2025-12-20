number = []
for index in range(3):
    item = int(input("Enter a number: "))
    number.append(item)
sums = number[0]+number[1]+number[2]
print(f"The average of the numbers is {round(sums/3,2)}")