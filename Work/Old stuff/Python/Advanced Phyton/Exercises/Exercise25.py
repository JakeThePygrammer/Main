def addingnumbers(n, m):
    finalresult = 0
    for i in range(n, m+1):
        finalresult += i
    return finalresult

print(addingnumbers(int(input("Enter a number : ")), int(input("Enter a number : "))))
