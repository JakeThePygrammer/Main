def calc(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "Invalid operator!"

a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
op = input("Enter a math operator(+,-,*,/) : ")
print(f"The answer is : {calc(a,b,op)}")