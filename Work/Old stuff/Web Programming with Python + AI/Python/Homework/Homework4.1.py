import random
list1 = []
total = 0
max_amount_seen = 0
for index in range(20):
    list1.append(random.randint(1,6))

for item in list1:
    total += item

for index in range(1, 7):
    amountseen = list1.count(index)
    if amountseen > max_amount_seen:
        max_amount_seen = amountseen
        commonnumber = index

print(f"The number six has appeared {list1.count(6)} times.")
print(f"The most shown has appeared {max_amount_seen} times. It is the number {commonnumber}.")
print(f"The average is {total/20}")