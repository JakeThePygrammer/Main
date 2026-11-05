import sys
data = sys.stdin.read().split()

for i in data:
    if int(i) <= 2:
        print("SAFE")
    elif int(i) > 2 and int(i) <= 4:
        print("WARNING")
    elif int(i) > 4:
        print("BLOCKED")


