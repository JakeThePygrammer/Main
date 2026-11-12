import hashlib

original = input("Enter your message: ")
modified = input("Enter the other persons message: ")

originalhash = hashlib.sha256(original.encode()).hexdigest()
modifiedhash = hashlib.sha256(modified.encode()).hexdigest()

if originalhash == modifiedhash:
    print("Message integrity verified!")
else:
    print("WARNING: Message has been modified!")