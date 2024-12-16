import random
f = open("Exercise14.txt", "w")
for index in range(10):
    n = random.randint(1,35)
    f.write(f"{str(n)}\n")
f.close()
f = open("Exercise14.txt", "r")
lines = f.readlines()
small = 36
large = 0
for line in lines:
    if int(line) > large:
        large = int(line)
    else:
        if int(line) < small:
            small = int(line)
print(f"{small} is the smallest number")
print(f"{large} is the largest number")


