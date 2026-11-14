import secrets
import sys
from datetime import datetime, timedelta

a = input("Enter your username: ")
secret = secrets.token_urlsafe(16)
expiration_time = datetime.now() + timedelta(seconds=10)
print(f"Password reset link : skopjephotography.com/{secret}")
tokeninsert = input("Enter your reset token: ")
b = secrets.compare_digest(tokeninsert, secret)
for index in range(2):
    if b and expiration_time > datetime.now():
        print("Password reset approved!")
        sys.exit()
    elif expiration_time < datetime.now():
        print("Token expired!")
        sys.exit()
    else:
        print("Wrong token! Try again!")
        tokeninsert = input("Enter your reset token: ")
        b = secrets.compare_digest(tokeninsert, secret)
print("Too many failed attempts!")
