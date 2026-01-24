def lettercounter(text, letter):
    count = 0
    for index in range(len(text)):
        if text[index] == letter.upper() or text[index] == letter.lower():
            count += 1
    return count

a = input("Enter some text : ")
b = input("Enter a letter : ")
print(f"The letter {b} appears {lettercounter(a,b)} times.")