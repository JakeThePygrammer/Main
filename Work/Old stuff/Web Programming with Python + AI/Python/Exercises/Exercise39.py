def above10(list1):
    tally = 0
    for index in list1:
        if index > 10:
            tally += 1
    return tally

a = int(input("How many values do you want to enter : "))
list1 = []
for index in range(a):
    list1.append(int(input("Enter a number : ")))

print(f"Of the values entered, {above10(list1)} were above 10.")