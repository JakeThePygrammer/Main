import sys

data = sys.stdin.read().split()
numberofitems = int(data[0]) + 1
dangerous = ["exe", "bat", "cmd", "vbs", "scr"]
counter = 0
for i in range(1, numberofitems):
    temp = data[i]
    templist = temp.split(".")
    if templist[- 1].lower() in dangerous:
        print(templist[0] + "." + templist[1])
        counter += 1

if counter == 0:
    print("NONE")
