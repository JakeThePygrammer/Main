file = open("../Text files/Exercise48Text.txt", "r")
tallyeven = 0
tallyodd = 0
countereven = 0
counterodd = 0
for line in file:
    if int(line) % 2 == 0:
        tallyeven += int(line)
        countereven += 1
    if int(line) % 2 != 0:
        tallyodd += int(line)
        counterodd += 1

print(f"The average of the even numbers is : {tallyeven / countereven}")
print(f"The average of the odd numbers is : {tallyodd / counterodd}")

file.close()