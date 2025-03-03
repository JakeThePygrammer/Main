numberlist = []
for i in range(5):
    numberlist.append(int(input("Enter a number:")))
numberlist.sort()
print(numberlist)
#Вака можеме да ставиме повеќе броеви во листа и да ги подредиме по големина. Се користи sort.

class Student:
    def __init__(self,name = 'enter',age = 'enter'):
        self.name = name
        self.age = age
    def greet(self):
        print("Hello everyone my name is " + self.name)
    def increaseAge(self):
        self.age = self.age + 1
    def __str__(self):
        return f"Student."


student1 = Student('Jakov',11)
student2 = Student('Ana', 12)
print(isinstance(student2,Student))
student2.greet()
student1.increaseAge()
#Вака се прават и се користат класи.isinstance враќа true или false.

text = "From blagoja.todorovska@gmail.com Sat Jun 6 09:30:25 2025"
index_second_space = text.find("fr", 10)
text.lower()
print(text[index_second_space])
#Ова е како се наоѓаат работи со find функцијата.

import string
from datetime import datetime

print(f"Letters {string.ascii_lowercase}")

dateandtime = datetime(year = 2024, month = 10, day = 5, hour = 12, minute = 42)
print(dateandtime)
date = "5-10-2024 12:46"
date_object = datetime.strptime(date,"%d-%m-%Y %H:%M")
print(date_object)

#Време и дата

f = open("text1.txt", "r")

lines = f.readlines()
print(lines[2:])

import random
a = random.randint(20,100)
print(a)

#Рандомизирање
try:
    delenik = int(input("Enter the first number of the division: "))
    delitel = int(input("Enter the second number of the division: "))
    rezultat = delenik / delitel
    print(rezultat)
except ZeroDivisionError as e:
    print("You cannot divide by 0!")
    print(e)
except ValueError as f:
    print("Please enter numbers.")
    print(f)
except Exception as g:
    for index in range(100):
        print("Unknown error!")
else:
    print("The program finished successfully.")
finally:
    print("Ths will always print.")
