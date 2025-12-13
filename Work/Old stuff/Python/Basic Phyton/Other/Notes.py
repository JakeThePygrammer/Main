cd = ("klm")
print(cd)
#Може да работи вака.
! = ("abc")
print(!)
#Не може бидејки мора да нема специјални карактери.
1 = ("def")
print(1)
#Не може да почне со број.
int = ("efg")
print(int)
#Не може да се користат работи како int бидејЌи се користат во кодот.
a b = ("hij")
print(a b)
#Не може да се користат празни места. Како замена се користи underscore _.
abc = int("100.10")
print =(abc)
#Int дава само цели броеви. Ќе се испринта грешка. Место int може вака a = 100. Ова се гледа како интеџер.
a = float(5.1)
print(a)
#Со float ова ќе биде 5.1.
a = 15
a -= 10
print(a)
#а ќе испринта 5 бидејќи ќе се одземе 10.
#Има и други вакви како += собирање, *= множење, /= делење, %= остаток од делење со тој број, // колку пати се содржи еден број во друг, **= на квадрат.
a = list("kniga")
print(a)
#Ова ќе се испринта ['k', 'n', 'i', 'g', 'a'], бидејќи се користи list.
a = 10
print("num is",a)
#Ова ќе се испринта "num is 10".
a = 15
b = 10
print (int(a/b))
#За да не ги гледаме децималите може вака.
bool_1 = True
bool_2 = False
#Bool може да е само false или true.
cd = ("klm")
print(type(cd))
bool_2 = False
print(type(bool_2))
#Type кажува што е тоа. Ова ќе биде str, bool.
Name = "Jakov "
Surname = "Nestorovski."
print(Name + Surname)
#Вака се принтаат сите заедно, но без празни места, затоа памти да додадеш
greater = 10 > 5
print(greater)
#Ова ќе даде true.
greater = 1 > 5
print(greater)
#А ова false.
tekst_1 = "12345"
print(len(tekst_1))
#Ова ќе испринта колку бројќи и букви има. Мора да е str.
name="Jake Nestor"
name2=(name).replace("Jake","Jakov")
print(name2)
#Ова ќе се испринта Jakov Nestor.
print("abc".upper())
print("ABC".lower())
print("gheqfuiw".capitalize())
#Буквите upper ги прави големи, lower мали,a capitalise само првата буква ја прави голема.
class_list = ["peter", "james" ,"ana" ,"annie"]
print(class_list)
#Ова ќе ги испринта децата во листата. Листи содржат повеќе работи. Секој член има бројка, од 0. Ова се вика индексирање.
#Во листи може да ги има сите видови елементи. Ова дава и листи во листи. Во листи ако има дупли елементи само првиот се принта.
print(class_list[3])
#За да се испринта само еден член, оди вака. Ова ќе испринта annie.
class_list = ["peter", "james" ,"ana" ,"annie"]
print(class_list)
class_list.pop(2)
print(class_list)
#За вадење елементи се користи pop. Овде се вади ana. Може и remove("ana")
class_list = ["peter", "james" ,"ana" ,"annie"]
class_list.extend(["jonah", "jana"])
print(class_list)
#За додавање повеќе елементи се користи ова. Append дава само еден.
a = "55"
print(a.isdigit)
#Ова проверува дали е број. Ова само работи со string.
a = " ten "
print(len(a.strip()))
#Ова вади празни места на крајот и на почетокот. Ова ќе искочи 3. lstrip и rstip вадат само од левата и од десната страна.
people = ("Me", "Jonah", "Ana")
print(people)
print(type(people))
#Ова е tuple. Може дупликати, но вредноста на елементи не може да се промени. Има индексирање[], и имаат редослед. За само еден елемент мора вака: people = ("Me",)
people = {"Me", "Jonah", "Ana"}
print(people)
print(type(people))
#Ова е set. Нема редослед, вредноста на елементи не се менува, но може да се додаваат и одземаат елементи со .remove и .add, нема индексирање, неможе дупликати, и загради се овие {}.
countriescities = {"macedonia":"skopje","france":"paris"}
print(countriescities)
print(type(countriescities))
print(len(countriescities))
#Ова е dictionary. Може дупликатни елементи, но не исти клучеви. Не се индексирани, и нема редослед. Ова ќе се испринта 2 елементи.
keys = ("name", "surname", "favorite colour","phone","home country","school")
values = ("Jakov", "Nestorovski", "Blue","Samsung Galaxy S21","Macedonia","OOU Lazo Angelovski")
dictionary = dict(zip(keys,values))
print(dictionary)
#Овие tuples ќе направат еден dictionary.
intger = 32
flt = 3.2
my_sum = intger + flt
print(my_sum)
print(type(my_sum))
#Ова е implicit conversion, ова само работи со float и integer. Ова ќе искочи float.
intger = 32
flt = float("3.2")
my_sum = intger + flt
print(my_sum)
print(type(my_sum))
#Ова е explicit conversion, ова дава и str.
print("Enter a number")
a = int(input())
print("Enter another number")
b = int(input())
if a < b:
    print(a, "is smaller than", b)
elif a == b:
    print(a, "is equal to", b)
else:
    print(a, "is larger than", b)
#Ова е if statment. Ова го проверуба твојот услов, и ако е точен, ја врши акцијата. Elif врши друго. Оператори за споредување се : > < == <= >=.
print("Vnesi broj")
a = int(input())
if a%2 == 0:
    print("Brojot e paren")
else:
    print("Brojot e neparen")
#Проверка за парен или непарен број.
a = 10
while a > 0:
    print(a)
    a -= 1
    continue
else:
    print("no more")
#Ова е while јамка. Ова дава работи да се повторуваат повеќе пати. Ова ќе работи 10 пати.
a = 10
while a > 0:
    if a == 3:
        a += 1
        continue
    print(a)
    a -= 1
    continue
#Ова се користи за скипање.
shows = ["young sheldon", "big bang theory", "the office", "superstore"]
for show in shows:
    print(show)
#Ова е for loop, ги брои сите ементи пр: index in range.
shows = ["young sheldon", "big bang theory", "the office", "superstore"]
for index in range(a,b,c):
    print(shows[index])
#a = старт b = крај c = чекор на изминување
shows = {"young sheldon" : "sheldon", "the office" : "Michael","superstore" : "Jonah, Amy "}
print("Everything in the list:")
for key,value in shows.items():
    print(key,value)

print("\nAll the keys:")
for keys in shows.keys():
    print(keys)

print("\nAll the values:")
for values in shows.values():
    print(values)
#Со dictionary треба додатоци на крајот.\n додава празен ред. За да нема торка стави key, value.
shows = ["young sheldon", "big bang theory", "the office", "superstore"]
for index in range(4):
    if index <= 1:
        print(shows[index])
    else:
        break
#Вака може да се заврши пред сите елементи. Ова се добива со break.
shows = ["young sheldon", "big bang theory", "the office", "superstore"]
for index in range(4):
    if index == 2:
        continue
    print(shows[index])
#Вака се скипаат елементи. Ова се добива со continue. Овде се вади the office.
shows = ["young sheldon", "big bang theory", "the office", "superstore"]
for index in range(len(shows)):
    if shows[index] == "the office":
        break
    print(shows[index])
#Вака се застанува со посебен елемент.Break може да се замени со continue и да работи.
len() range() input() print()
#Ова се функции, овие се неколку интегрирани функции.
def printing(name = "Enter a name"):
    print(name)
    print("A name")
printing("Sheldon")
printing("Amara")
print("Some names")
#Ова се кориснички функции, тие се направени од корисници.
def sum3 (a,b,c)
    return a+b+c
sum3(3,6,9)
#Може да има повеќе елементи.
def sum3 (a,b,c):
    """here you add a+b+c"""
    return a+b+c
suma = sum3(3,6,9)
#Вака може да се префли резултатот во променлива.
def sum3 (a,b,c):
    """Using this function, you add 3 numbers together. These are marked with a,b and c."""
    return a+b+c
suma = sum3(3,6,9)
print(sum3.__doc__)
print(suma)
#Ова е doc string.Ова е за девелопери.