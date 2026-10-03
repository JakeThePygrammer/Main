list1 = []
for index in range(10):
    a = int(input("Enter a number: "))
    list1.append(a)
largest = 0
for index in range(1,10):
    if list1[index] > largest:
        largest = list1[index]

print(f"The largest value in the entered list is {largest}")