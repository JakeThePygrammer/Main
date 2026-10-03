def vowelcounter(text):
    count = 0
    text1 = text.lower()
    for index in range(len(text)):
        if text1[index] == 'a' or text1[index] == "e" or text1[index] == "i" or text1[index] == "o" or text1[index] == "u":
            count += 1
    return count

a = input("Enter some text : ")
print(f"Vowels appear {vowelcounter(a)} times in the text.")