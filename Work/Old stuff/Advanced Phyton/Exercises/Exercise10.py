f = open("Exercise10.txt", "r")
lines = f.readlines()
for line in lines:
    print(line.upper())