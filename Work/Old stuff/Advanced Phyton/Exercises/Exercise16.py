numbers = []
for index in range(5):
    try:
        a = int(input("Enter a number : "))
        numbers.append(a)
        print("Number entered successfully")
    except ValueError:
        print("Please enter numbers. Program cancelled")
        break
print(f"Your numbers are : {numbers}")