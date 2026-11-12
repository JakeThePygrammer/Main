import secrets
import string
import random

def createsecurepassword(length = 12):
    if length < 12:
        length = random.randint(12,25)
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    list = lowercase + uppercase + digits + special
    while True:
        b = ""
        for i in range(length):
            b = b + secrets.choice(list)
        lowercasecheck = False
        uppercasecheck = False
        digitcheck = False
        specialcheck = False
        counter = 0
        while counter < len(b):
            if b[counter] in lowercase:
                lowercasecheck = True
            if b[counter] in uppercase:
                uppercasecheck = True
            if b[counter] in digits:
                digitcheck = True
            if b[counter] in special:
                specialcheck = True
            counter = counter + 1
        if lowercasecheck and uppercasecheck and digitcheck and specialcheck:
            return b
        else:
            continue

a = int(input("Enter password length(min 12): "))
c = createsecurepassword(a)
print(f"Your password is: {c}")