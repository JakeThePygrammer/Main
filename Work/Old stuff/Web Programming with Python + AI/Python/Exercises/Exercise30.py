secretnumber = 43
inputnumber = 0
counter = 0
while secretnumber != inputnumber:
    inputnumber = int(input("Enter a number: "))
    counter += 1
print(f"You guessed {counter} times.")