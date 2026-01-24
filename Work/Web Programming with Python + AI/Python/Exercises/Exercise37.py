def lettercounter(text):
    count = 0
    for index in range(len(text)):
        if text[index] == "J" or text[index] == "j":
            count += 1
    return count

a = input("Enter some text : ")
print(f"The letter J appears {lettercounter(a)} times.")