def makenumlist(list):
    numlist = []
    for element in list:
        if element % 2 == 0:
            numlist.append(element)
    return numlist
def checkwordlength(words):
    textofwords = words.split()
    exit = []
    for words in textofwords:
        if len(words) >= 5:
            exit.append(words)
    return exit
def squarednumberinput(numbers):
    squarednumbers = []
    for number in numbers:
        squarednumber = number * number
        squarednumbers.append(squarednumber)
    return squarednumbers
