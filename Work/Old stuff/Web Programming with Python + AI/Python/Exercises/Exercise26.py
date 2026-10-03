for index in range(1,51):
    if index % 3 == 0 and index % 5 == 0:
        print(f"{index} FizzBuzz")
    elif index % 3 == 0:
        print(f"{index} Fizz")
    elif index % 5 == 0:
        print(f"{index} Buzz")