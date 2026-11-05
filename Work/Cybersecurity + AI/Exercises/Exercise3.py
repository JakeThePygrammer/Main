import sys

data = sys.stdin.read().split()
dictattempts = {}
dictattemptskeys = []
counter = 0
for i in range(1, len(data), 2):
    dictattemptskeys.append(data[i])

dictattempts = dict.fromkeys(dictattemptskeys, 0)

for i in range(2, len(data), 2):
    if data[i] == "FAIL":
        dictattempts[data[i - 1]] += 1

for key, value in dictattempts.items():
    if value >= 3:
        print(key)
        counter += 1
if counter == 0:
    print("NONE")





