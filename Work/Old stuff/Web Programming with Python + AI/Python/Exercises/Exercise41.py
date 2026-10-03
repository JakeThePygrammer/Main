def hiddenword(word):
    a = len(word)
    return word[0] + (a-1) * "*"

a = input("Enter a word : ")
print(f"Your word hidden is : {hiddenword(a)}")

def guesser(correct_word, guess):
    if correct_word == guess:
        return "Your guess was correct! Congratulations!"
    else:
        return "Your guess was incorrect! Try again!"

ab = input("Enter your guess : ")
ab = ab.lower()
a = a.lower()
print(guesser(a, ab))