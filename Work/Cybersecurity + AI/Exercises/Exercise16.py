from cryptography.fernet import Fernet
from datetime import datetime, timedelta
key = Fernet.generate_key()
f = Fernet(key)
a = input("Enter a mesage to encrypt: ")
a = a.encode("utf-8")
token = f.encrypt(a)
expiration_time = datetime.now() + timedelta(seconds=10)
input("Press Enter to continue: ")
if expiration_time > datetime.now():
    print(f.decrypt(token))
else:
    print("The time has ended!")