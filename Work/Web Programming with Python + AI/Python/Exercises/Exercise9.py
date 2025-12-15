text = input("Enter some text: ")
textlenhalf = len(text)//2
print(f"First half of text : {text[:textlenhalf].upper()}")
print(f"Second half of text : {text[textlenhalf:].lower()}")