a = input("Enter a word: ")
b = 0
for index in range(len(a)):
    if a[index] == "a":
        b += 1
else:
    print(f"{a} has {b} A's.")
