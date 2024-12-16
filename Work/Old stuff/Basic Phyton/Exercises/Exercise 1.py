print("Enter a language: english, Внеси јазик: македонски")
c = input()
if c == ("english"):
    #Оригинално.
    print("Enter a number:")
    a = int(input())
    b = 15
    print("Your number will do calculations with",b)
    print("Addition:",a+b)
    print("Subtraction:",a-b)
    print("Multiplication:",a*b)
    print("Division:",a/b)
    print("Squared:", a**b)
    print("Done!")
    #Ново.
if c == ("македонски"):
    print("Внеси број:")
    a = int(input())
    b = 15
    print("Твојот број ќе прави калкулации со", b)
    print("Собирање:", a + b)
    print("Одземање:", a - b)
    print("Множење:", a * b)
    print("Делење:", a / b)
    print("На квадрат:", a ** b)
    print("Готово!")