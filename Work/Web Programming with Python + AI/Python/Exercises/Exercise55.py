import random
names = ["James", "John", "Mark", "Rick", "Taylor", "Ted", "Robin", "Barney", "Joey", "Jessica"]
while names != []:
    a = random.choice(names)
    print(a)
    b = input("Keep(y) or remove(n) the name : ")
    if b =="n":
            names.remove(a)
if names == []:
    print("No names are left")
