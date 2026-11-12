import secrets
import sys

a = input("Enter your username: ")
secret = secrets.token_urlsafe(16)
print(f"Password reset link : skopjephotography.com/{secret}")
tokeninsert = input("Enter your reset token: ")
b = secrets.compare_digest(tokeninsert, secret)
for index in range(2):
    if b:
        print("Password reset approved!")
        sys.exit()
    else:
        print("Wrong token! Try again!")
        tokeninsert = input("Enter your reset token: ")
        b = secrets.compare_digest(tokeninsert, secret)
print("Too many failed attempts!")
