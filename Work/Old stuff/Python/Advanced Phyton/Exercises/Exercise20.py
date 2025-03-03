def subtraction(a,b):
    print(f"{a} minus {b} is {a - b}")
def division(a,b):
    print(f"{a} divided by {b} is {a/b}")
operation = input("Enter if you would like to divide or subtract. Use signs to choose(-,/) : ")
try:
    num1 = int(input("Enter a number : "))
    num2 = int(input("Enter a number : "))
except ValueError:
    print("Please enter numbers.")
try:
    if operation == "-":
        subtraction(num1,num2)
    elif operation == "/":
        division(num1,num2)
    else:
        print("Please enter a valid operation.")
except ZeroDivisionError:
    print("Divided by zero.")
except NameError:
    print("One of the numbers was not entered/was put in as a letter.")
