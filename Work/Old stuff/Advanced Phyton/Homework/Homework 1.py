a = int(input("Enter a number "))
for index in range(2,a):
    if a % index == 0:
        print("Your number is not prime")
        break
else:
    print("Your number is prime")