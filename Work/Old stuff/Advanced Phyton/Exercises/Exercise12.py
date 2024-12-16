f = open("Exercise12.txt", "r")
lines = f.readlines()
value = 0
for line in lines:
    value += int(line)
print(value)