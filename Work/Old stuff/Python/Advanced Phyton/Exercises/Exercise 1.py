numberlist = []
for i in range(5):
    numberlist.append(int(input("Enter a number: ")))
numberlist.sort()
for i in range(5):
    if numberlist[i] % 2 == 0:
        numberlist[i] *= 3
    else:
        numberlist[i] /= 2
print(f"Entered numbers: {numberlist}")
