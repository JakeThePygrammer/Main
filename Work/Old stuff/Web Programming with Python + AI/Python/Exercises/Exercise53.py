import random
guessthis = random.randrange(1,101)
guessednumber = 0
counter = -1
while guessthis != guessednumber:
    counter += 1
    guessednumber = int(input("Guess the number: "))
print(f"The number was {guessthis}! You guessed wrong {counter} times!")
