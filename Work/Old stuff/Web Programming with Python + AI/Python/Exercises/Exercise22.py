numdict = {}
text = input("Enter some text: ")
textlist = text.split(" ")
for word in textlist:
    if word not in numdict:
        numdict[word] = 1
    else:
        numdict[word] += 1

for word in numdict.keys():
    if numdict[word] != 0:
        print(f"For the word {word} there are {numdict[word]} occurrences.")