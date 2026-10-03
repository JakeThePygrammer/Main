file = open("../Text files/Exercise51Text.txt", "r")
list1 = file.readlines()
file.close()

file = open("../Text files/Exercise51Text.txt", "w")
for index in range(3):
    list1.append(input("Enter a name : "))
list1.sort()
for item in list1:
    file.write(f"{item.capitalize()}\n")