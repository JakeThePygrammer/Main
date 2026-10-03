operation = ""
num1 = 0
num2 = 0
switch = True
while switch == True:
    operation = input("Enter an operator(+,-,*,/) or 'exit' to exit: ")
    if operation == "exit":
        switch = False
    else:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        if operation == "+":
            result = num1 + num2
        if operation == "-":
            result = num1 - num2
        if operation == "*":
            result = num1 * num2
        if operation == "/":
            result = num1 / num2
        print(f"The result is {result}")
