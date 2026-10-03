import random

list1 = ["communism","democracy","socialism","capitalism"]

a = random.choice(list1)
b = list(a)

print("The scrambled word is : ", end="")

random.shuffle(b)

for index in range(len(a)):
    print(b[index], end="")

print("\n")

counter = 0

for index in range(3):
    if input(f"Guess the word : ") == a:
        print(f"Correct! The word is {a}! It took you {counter+1} times.")
        break
    else:
        counter += 1

if counter == 3:
    print(f"You didn't guess the word correctly. The word was {a}.")