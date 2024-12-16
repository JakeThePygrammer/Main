numbers = []
try:
    n = int(input("Enter how may numbers you want to add : "))
except ValueError as f:
    print("Please enter a number.")
    print(f)
else:
    for index in range(n):
        try:
            a = int(input("Enter a number : "))
            numbers.append(a)
        except ValueError as f:
            print("Please enter a number.")
            print(f)
        finally:
            print("Number entered successfully")
    try:
        print(f"{numbers[9]} is the tenth number of your entered numbers.")
    except IndexError:
        print(f"{numbers[-1]} is the last number of your entered numbers. This is because you entered less than 10 numbers.")