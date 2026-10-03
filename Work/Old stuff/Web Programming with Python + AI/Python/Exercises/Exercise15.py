testpoints = int(input("Enter number of points gotten on the test: "))

if testpoints >= 90:
    print("The grade according to the points is an A")
elif testpoints >= 75:
    print("The grade according to the points is an B")
elif testpoints >= 60:
    print("The grade according to the points is an C")
elif testpoints >= 40:
    print("The grade according to the points is an D")
else:
    print("The grade according to the points is an F")