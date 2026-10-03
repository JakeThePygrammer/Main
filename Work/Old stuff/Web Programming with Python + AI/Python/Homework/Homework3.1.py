def firstencrypt(a):
    encrypted = ""
    for index in a:
        if index.isdigit():
            encrypted = encrypted + "8"
        elif index.isalpha():
            encrypted = encrypted + "6"
        else:
            encrypted = encrypted + "1"
    return encrypted

def secondencrypt(a):
    encrypted = ""
    for index in a:
        if index.isalpha():
            encrypted = encrypted + "1"
        else:
            encrypted = encrypted + "0"
    return encrypted

def finalencrypt(a):
    encrypted = ""
    encrypted = firstencrypt(a) + secondencrypt(a)
    return encrypted

print(f"The encrypted value is : {finalencrypt(input("Enter text: "))}")
