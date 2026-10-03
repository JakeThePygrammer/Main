def triangle(number):
    for i in range(1, number + 1):
        print("")
        print("#", end="")
        for j in range(1, i + 1):
           print(j, end="")

triangle(int(input("Enter a number : ")))