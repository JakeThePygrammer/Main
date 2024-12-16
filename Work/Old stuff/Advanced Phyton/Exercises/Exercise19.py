food = ["chocolate","chicken","corn","sandwich","soup","potatoes","beef","lox","lemonade"]
fifth = []
for index in food:
    try:
        fifth.append(index[4])
    except IndexError:
        print(f"{index} is smaller than 5 letters.")
print(f"{fifth}. These are the fifth letters in all the words in the list.")