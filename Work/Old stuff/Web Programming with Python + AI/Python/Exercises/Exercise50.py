file = open("../Text files/Exercise50Text.txt", "a")
n = int(input("How many phone numbers would you like to add : "))
text = ""
for index in range(n):
    a = (f"{input(f"Enter name {index + 1} : ")}")
    b = (f"{input(f"Enter surname {index + 1} : ")}")
    c = (f"{input(f"Enter phone number {index + 1} : ")}")
    file.write(f"{a.capitalize()} {b.capitalize()} : {c}\n")
file.close()
