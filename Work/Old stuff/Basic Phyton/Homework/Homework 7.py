def check(start,end,number):
    for index in range(start,end):
        if number == index:
            print("Your number is in the interval")
            break
    else:
        print("Your number is not in the interval")

begin = int(input("Enter the start of the interval "))
stop = int(input("Enter the end of the interval "))
choice = int(input("Enter the number you want to check to see if it's in the interval "))
check(begin,stop,choice)
