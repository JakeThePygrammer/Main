def palindromechecker(word):
    if word.lower() == word[::-1]:
        return True
    else:
        return False

