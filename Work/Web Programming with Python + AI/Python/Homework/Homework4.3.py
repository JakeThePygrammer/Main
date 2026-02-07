import random

list3 = random.sample(range(1,30), k = 5)
list2 = []
tally = 0

for index in range(len(list3)):
    a = int(input("Enter a number : "))
    if a in list3:
        list2.append(a)
        tally += list3.count(a)

print(f"You guessed {tally} numbers!")
print("The numbers you guessed are : ")
for number in list2:
    print(number)