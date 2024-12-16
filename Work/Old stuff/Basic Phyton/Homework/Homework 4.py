a = 1
while a == 1:
    print("Enter password")
    b = input()
    if b == "3124":
        print("Password is correct!")
        break
    else:
        print("Password is incorrect! Try again.")
        continue