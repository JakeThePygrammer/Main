N = int(input("Enter a number: "))
tally = 0
for index in range(1,N+1):
    tally += index
print(f"The tally of all the numbers from 1 to {N} is {tally}")