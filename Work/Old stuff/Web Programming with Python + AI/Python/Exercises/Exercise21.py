numdict = {}
text = input("Enter some text: ")
textlist = text.lower()
for letter in textlist:
    if letter not in numdict:
        numdict[letter] = 1
    else:
        numdict[letter] += 1

for letter in numdict.keys():
    if numdict[letter] != 0:
        print(f"For the letter {letter} there are {numdict[letter]} occurrences.")