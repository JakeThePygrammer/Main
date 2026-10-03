import random
guessthis = random.randrange(1,101)
guessednumber = 0
guessedlist = []
counter = 0
while counter <= 20:
    guessednumber = int(input("Guess the number: "))
    if guessthis == guessednumber:
        print(f"The number was {guessthis}! You guessed wrong {counter} times!")
        break
    elif guessednumber in guessedlist:
        print(f"The number {guessednumber} has already been guessed!")
        counter -= 1
    else:
        print("Try again!")
        guessedlist.append(guessednumber)
    counter += 1




