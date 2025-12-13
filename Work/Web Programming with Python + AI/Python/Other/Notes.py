#When printing, you can use either " or ', but make sure that if you start with one, you finish with it too.

print("Hello World")
print('Hi again!')

#Empty variables dont exist, but variable types don't need to be defined. From symbols you can only use underscore(_).

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
#Operators for math
# / - division returns float
# //- division returns integer(removes the decimal part)
# % - returns the remainder of the division
# + - addition
# - - subtraction
# * - multiplication
# ** - 1st number is base, 2nd is power(2**3 is 2 to the power of 3)
#Check exercise 1 for use case

num1 = int(input("Enter a number: "))   #int variable change can go at input or at operation
num2 = input("Enter another number: ")
total = num1 + int(num2)    #int variable change can go at input or at operation
print(f"The total of your numbers is : {total}")