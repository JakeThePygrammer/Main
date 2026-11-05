import sys

data = sys.stdin.read().split()
safe = True
words = ["urgent", "password", "verify", "winner", "prize"]
for item in data:
    itemlower = item.lower()
    for word in words:
        if word in itemlower:
            safe = False
            break
if safe:
    print("SAFE")
else:
    print("SUSPICIOUS")

