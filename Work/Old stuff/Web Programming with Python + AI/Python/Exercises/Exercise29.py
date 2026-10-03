start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
x = start
tally = 0
while x <= end:
    tally += x
    x += 1

x -= 1
average = tally / x


print(f"The average of the range is {average} and the sum of the range is {tally}")
