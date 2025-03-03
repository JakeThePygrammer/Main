num = 0
a = input("Enter a word ")
for word in a:
    if word == "a":
        num += 1
    elif word == "e":
        num += 1
    elif word == "i":
        num += 1
    elif word == "o":
        num += 1
    elif word == "u":
        num += 1
    else:
        continue
print("The number of vowels in your letter is :", num)