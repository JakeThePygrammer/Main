import sys

data = "sys.stdin.read().split()"

datalist = data[0].split(".")
valid = "VALID"

if len(datalist) == 4:
    for item in datalist:
        if not item or not item.isdigit():
            valid = "INVALID"
            break
        if len(item) > 1 and item[0] == "0":
            valid = "INVALID"
            break
        if not 0 <= int(item) or not int(item) <= 255:
            valid = "INVALID"
            break
else:
    valid = "INVALID"

print(valid)