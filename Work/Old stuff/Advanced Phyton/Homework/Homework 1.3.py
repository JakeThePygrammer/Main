a = []
c = 0
for index in range(5):
    b = int(input("Enter a number "))
    a.append(b)
    c += b
a.sort()
print(f"Your numbers have been sorted: {a}")
print(f"Your smallest number is {a[0]}, and your largest number is {a[4]}")
print(f"All your number combined equal {c}")
print(f"The average of your numbers is {c/5}")
