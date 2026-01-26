def hiddenword(word,level):
    a = len(word)
    if level == "easy" or level == "Easy":
        return word[0] + (a - 2) * "*" + word[-1:]
    elif level == "medium" or level == "Medium":
        return word[0] + (a - 1) * "*"
    elif level == "hard" or level == "Hard":
        return a * "*"

answer = input("Enter a word : ")
levelhardness = input("Enter the level hardness(easy,medium,hard) : ")
print(f"Your word hidden is : {hiddenword(answer,levelhardness)}")

def guesser(correct_word, guess):
    counter = 0
    while True:
        if correct_word == guess:
            return f"Your guess was correct! Congratulations! You guessed the word {counter+1} times!"
        else:
            counter += 1
            print("Your guess was incorrect! Try again!")
            guess = input("Enter your guess : ").lower()


guess = input("Enter your guess : ")
guesslower = guess.lower()
answerlower = answer.lower()
print(guesser(answerlower, guesslower))