from datetime import datetime, time, date
username = input("Enter a username : ")
if not username.isalnum():
    username = input("Please enter another username : ")
date = input("Enter your date of birth : ")
date_object = datetime.strptime(date,"%d-%m-%Y")
emails = input("Enter an email : ")
if not emails[-3:] in [".mk", "com", "net"]:
    emails = input("Enter your email again : ")
if not "@" in emails:
    emails = input("Enter your email again : ")
information = {"Username": username,"Date of birth" : date_object, "Time of creation" : datetime.now(), "Email" : emails}
from datetime import datetime, time, date
username = input("Enter a username : ")
if not username.isalnum():
    username = input("Please enter another username : ")
date = input("Enter your date of birth : ")
date_object = datetime.strptime(date,"%d-%m-%Y")
emails = input("Enter an email : ")
if not emails[-3:] in [".mk", "com", "net"]:
    emails = input("Enter your email again : ")
if not "@" in emails:
    emails = input("Enter your email again : ")
information2 = {"Username": username,"Date of birth" : date_object, "Time of creation" : datetime.now(), "Email" : emails}
if information["Date of birth"] < information2["Date of birth"]:
    print(f"{information["Username"]} is older than {information2["Username"]}")
else:
    print(f"{information2["Username"]} is older than {information["Username"]}")