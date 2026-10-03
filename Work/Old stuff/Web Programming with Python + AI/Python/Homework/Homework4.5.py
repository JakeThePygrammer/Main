import random

list1 = []
largerthan50 = 0
even = 0

for index in range(100):
    list1.append(random.randint(1, 100))
    if list1[index] % 2 == 0:
        even += 1
    if list1[index] >= 50:
        largerthan50 += 1

print(f"There are {largerthan50} numbers larger than 50")
print(f"There are {even} even numbers.")
list1.sort()
print(f"The smallest number is : {list1[0]}")
print(f"The largest number is : {list1[-1]}")
