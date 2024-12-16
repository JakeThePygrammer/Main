word = input("Enter some text ")
value = 0
letters = ""
text = word.lower()
for letter in text:
   counter = text.count(letter)
   if value < counter:
       value = counter
       letters = letter
print(f"The letter that appears the most is {letters}, it appears {value} times.")