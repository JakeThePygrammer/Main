def fizzbuzz(a,b):
    for index in range(a,b+1):
        if index % 3 ==  0 and index % 5 == 0:
            print(f"{index} - FizzBuzz")
        elif index % 5 == 0:
            print(f"{index} - Buzz")
        elif index % 3 == 0:
            print(f"{index} - Fizz")
        else:
            print(f"{index} - None")

a = int(input("Enter start of range : "))
b = int(input("Enter end of range : "))
fizzbuzz(a, b)