#Use import to import modules. You can also use from module import function for a specific function.
#Modules to use : math, random(random.choice/s for random letter), string(use list type with ascii)

a = 0
import random
while a != 100:
    a = random.randrange(0, 101, 5)
    print(a)

list = [0,1,2,3,4,5,6,7,8,9]
for index in range(len(list)):
    print(random.choices(list, weights=[10, 10, 10, 10, 10, 10, 10, 10, 10, 10], k=1)) #Weights - chance to pick that item. k - how many items to pick.

#When printing, you can use either " or ', but make sure that if you start with one, you finish with it too.

print("Hello World")
print('Hi again!')

#Empty variables don't exist, but variable types don't need to be defined. From symbols, you can only use underscore(_).

integertype = 1 #Whole numbers only
floattype = 1.0 #Allows for use of decimals
stringtype = "string123" #Text
booleantype = True #True/False

#There are multiple ways to combine in print, but these are the most used.

print("The string is equal to " + stringtype + ", that is all.") #With +
print(f"The string is equal to {stringtype}, that is all.")      #With fstring

#Use type(variable) to get variable type.

print(f"The variable type is equal to {type(integertype)}") #Checks the type of the value(integer)

#isinstance(variable) checks the filetype.

print(f"The variable type is integer? {isinstance(integertype, int)}")

#In inputs with math, remember to change the value types to int, or use float for decimals
#There exist other operators such as str to turn into string
#Operators for math
# / - division returns float
# //- division returns integer(removes the decimal part)
# % - returns the remainder of the division
# + - addition
# - - subtraction
# * - multiplication
# ** - 1st number is base, 2nd is power(2**3 is 2 to the power of 3)
#Check exercises 1 - 3 for use cases

num1 = int(input("Enter a number: "))   #int variable change can go at input or at operation
num2 = input("Enter another number: ")
total = num1 + int(num2)    #int variable change can go at input or at operation
print(f"The total of your numbers is : {total}")

#String methods are used to change string values
#to use, write "value = othervalue.method()"
#upper() - sets all uppercase
#lower() - sets all lowercase
#capitalize() - sets first uppercase
#swapcase() - swaps lower and upper and vice versa
#title() - sets first letter of each word to uppercase
#count() - counts how much a specific character or word shows up in the string(put the character or word in the parentheses), case sensitive.
#startswith() - checks if the string starts with a specific character or word. Returns boolean value.
#endswith() - checks if the string ends with a specific character or word. Returns boolean value.
#isalpha() - checks if only letters(special character means false)
#isalnum() - checks for letters and numbers(spaces means false)
#isdigit() - checks for only numbers(spaces means false)
#islower() - checks if all lower(ignores special)
#isupper() - checks if all upper(ignores special)
#strip() - removes start and end spaces
#replace() - replaces something with something else(in parentheses put "chartoreplace", "charreplaced")
#len() - returns length of string(put variable in parentheses)
#split() - splits strings at the location of points
#, end == " " - allows for no insertion of new row when printing.
#Check exercises 4 - 8 and 18-19 for use cases

text = "abc def ghi"
count_a = text.count("a")
count_a_lower = text.lower().count("a") #Returns 1, lower can be removed, but better for accuracy
title_a = text.title()            #Returns "Abc Def Ghi"

#In strings, all characters have indexes.
#Positive indexes start from the start, they start from 0.
#Negative indexes start from the end, they start from -1, not from 0.
#They can be called like this : variable[index]

text = "abc def ghi"
print(text[1]) #Prints b

#Slicing is used for getting specific pieces of the text
#[start:end:step]
#Prints from the start(counting start(if start = 1 will start from 1)) to the end(not counting the end(if end = 3 will go to 2)
#Check exercises 9-11 for use cases

text = "abc def ghi"

print(text[1:3]) #prints bc
print(text[:3]) #prints abc
print(text[4:]) #prints from d to end
print(text[::-1])#prints reverse

#Use round(number, decimals) to round a number.

print(round(123.123, 2)) #returns 123.12

#Lists are variables with multiple items.
#Unlike C++, these lists can include different types of elements, and can always be changed.
#Using indexes is same as in strings
#Methods
#append(element) - adds new element at end
#insert(index) - inserts element at set location
#remove(element) - removes first occurrence of given element
#pop(index) - removes element at set location
#sort() - sorts with key
#len(list) - gives list length
#count(element) - counts the amount of a character or word in the list
#index(element) - gives the index of the first occurrence of the element, takes start - end args
#clear() - clears list
#reverse() - reverses list
#extend(list) - extends a list by adding another one to it
#Multiplying lists multiplies adds the whole list onto itself
#element not in/in list - returns true/false depending on if the element is/isn't in the list
#Check exercises 12-14 for use cases

list = [0,1,2,3,4,5,6,7,8,9]
print(list) #prints [0,1,2,3,4,5,6,7,8,9]
list.append(10)
print(list) #prints [0,1,2,3,4,5,6,7,8,9,10]
list.remove(10)
print(list) #prints [0,1,2,3,4,5,6,7,8,9]
list.pop(0)
print(list) #prints [1,2,3,4,5,6,7,8,9]
list.reverse()
print(list) #prints [9,8,7,6,5,4,3,2,1]

#Tuples are similar to lists, but the elements can't be changed.
#Methods
#count(element) - counts the amount of a character or word in the tuple
#index(element) - gives the index of the first occurrence of the element, takes start - end args
#element not in/in tuple - returns true/false depending on if the element is/isn't in the tuple
#Best for use in expected things such as days of the week
#Check exercise 17 for use case

tuple = (10,"a",True)
print(tuple)

#Sets have no indexes and no duplicates, albeit you can add and remove items.
#Methods
#add(element) - adds element at end
#remove(element) - removes element at end
#element not in/in set - returns true/false depending on if the element is/isn't in the set
# a | b - this returns all elements in both with no duplicates
# a & b - this returns what is in both a and b
# a - b - this returns what is in a and not in b

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B) # returns {1,2,3,4,5,6}
print(A & B) # returns {3,4}
print(A - B) # returns {1,2}

#Dictionaries have 2 value sets - keys and values
#The keys act as indexes
#You cannot have double keys
#dictionary[key] = element - add new values if new key, changes if key already exists
#pop(key) - removes element
#del dictionary[key] - removes element
#keys() - just the keys
#values() - just the values
#items() - returns pairs as tuple
#zip(list, list) - returns dictionary from 2 lists, add dict type marker
#element not in/in dictionary - returns true/false depending on if the element is/isn't in the dictionary

dictionary = {1:"A",2:"B",3:"C",4:"D",5:"E"}
print(dictionary)
print(dictionary[1]) #1 is a key, not an index
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
dictionary2 = dict(zip(["A", "B", "C"],[1,2,3]))
print(dictionary2)

#Once one is true, it exists the condition check, so watch out for the order of the statements
#if checks for true or false for a specific statement and runs if true
#elif for multiple conditions for different code
#else if all else fails
#Operators
#== - equal to
#!= - not equal to
#>= - greater or equal to
#<= - smaller or equal to
#> - larger than
#< - smaller than
#and/or - for multiple conditions for the same code
#element not in/in list/tuple/dictionary - returns true/false depending on if the element is/isn't in the list/tuple/dictionary
#pass - place after if/elif/else to not run anything
#Check exercises 15-17 and exercises 20-27(excluding 24)

a = int(input("Enter a number: "))
if a == 1:
    print("The number is equal to 1")
elif a == 2:
    print("The number is equal to 2")
else:
    print("The number is not equal to 1 or 2")

#Cycles are for running the same code multiple times, there are multiple types
#Use break to finish the cycle and continue to move to the next repetition
#You can do it with lists/tuples/dictionaries/strings written like this
#for element in list/tuple/dictionary/string:
#The element is the current one selected, so printing element would return the element at the position of what cycle the for cycle is on
#Another way is using index in range(numbers)
#This uses the same index rules as strings except if you only enter one number it would be considered as the end(start, stop, step)
#Check exercises 20-28 for use cases

for index in range(1,11):
    print(index)

#While cycles use an if statement to keep the cycle running
#While it's true, the cycle keeps running
#Since there are no indexes, you can use counters to know what cycle you're on.
#Use While True for an infinite cycle
#Use switches when there is more code
#Check exercises 30-33 for use cases

i = 0
while i <= 10:
    print(i)
    i += 1

#Functions are useful for calling predefined code. There are two types.
#Predefined functions are functions that are already built into python(print(), len()...).
#User-defined functions are functions that you create yourself.
#Use return to return the same as predefined functions, but print can be used too.
#Functions can exist without return and arguments, but without return, functions cannot be defined to a value(value will be None).
#Check exercises 34-43 for use cases.
#Defaut arguments can be set to making inserting items optional.

def functionName(arg1, arg2 = 1):
    return(arg1 + arg2)
print(f"Function result: {functionName(1, 2)}")
a = functionName(2, 2) #Value-defined function

#Keyword arguments are used for setting which parameter is for which value.
#This is useful in cases with default values.

def greeting(name, surname):
    print(f"Name = {name} Surname = {surname}.")

greeting(name = "Angela", surname = "Simonova")

#Docstrings are quick explanations of functions. Useful in multi-developer environments.

def greeting(name, surname):
    """
    :param name: name of user
    :param surname: surname of user
    :return: nothing
    this function isn't very important
    :D

    """
    print(f"Name = {name} Surname = {surname}.")

greeting(name = "Angela", surname = "Simonova")

#Multiple values can be returned using commas.

def calculations(a, b, ):
    return a + b, a - b
answer = calculations(1, 2) #Tuple
a1, a2 = calculations(1, 2) #2 values

#Lambda functions can run only one command, but can have infinite arguments.

x = lambda a, b: a + b #x is function name, then come the arguments, and finally the command.
print(f"The result is {x(5,6)}")

#Files store data.
#open(filename, mode) - opens a file.
#read(characteramount) - reads file.
#readline() - reads specific file line.
#readlines() - reads all file lines and puts them in list.
#You can use "for x in file" in for cycles.
#write("text") - adds to the end of the file.
#Modes:
#r - Read - opens file for reading. Cannot create new files.
#a - Append - opens a file for changes, creates new if file doesn't exist.
#w - Write - clears file for changes, creates new if file doesn't exist.
#x - Create - creates new file, error if already exists.
#Check exercises 48-XX for use cases

file = open("../Text files/NotesText.txt", "w")
for index in range(10):
    file.write(f"{input("Enter a number for the file : ")}\n")
file.close()

total1 = 0
filer = open("../Text files/NotesText.txt", "r")
filelist = filer.readlines()
for line in filelist:
    print(line, end="")
    total1 += int(line)
print(f"\nThe total of all the numbers in the file is : {total1}")
filer.close()

