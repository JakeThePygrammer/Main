from datetime import datetime, time, date

a = input("Enter your name and surname : ")
a = a.title()
a = a.split()
b = a[0]
c = a[1]
username = input("Enter a username : ")
if not username.isalnum():
    username = input("Please enter another username : ")
date = input("Enter your date of birth : ")
date_object = datetime.strptime(date,"%d-%m-%Y")
age = input("Enter your age : ")
if not age.isdigit():
    age = input("Enter your age again : ")
information = {"Username": username, "Name" : b, "Surname" : c, "Age" : age,"Date of birth" : date_object, "Time of creation" : datetime.now()}
print(information)