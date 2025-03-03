print("Enter a sentence:")
a = input()
print("Enter another sentence:")
b = input()
print("We will print the longer sentence.")
if len(a) < len(b):
    print(b)
elif len(a) == len(b):
    print("They have an equal length")
else:
    print(a)