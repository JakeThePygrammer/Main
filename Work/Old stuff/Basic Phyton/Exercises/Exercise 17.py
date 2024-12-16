numlist = [1412,1255,1566,4598,1251,1532,1563,1245,1556,1345]
a = int(input("Enter a 4 digit number: "))
for i in numlist:
    if i == a:
        print("The number is in the list!")
        break
else:
    print("The number is not in the list.")