f = open("Exercise11.txt", "r")
lines = f.readlines()
for line in lines:
    print(int(line)**2)