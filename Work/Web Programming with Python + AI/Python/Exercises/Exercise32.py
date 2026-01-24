inputnumber = 0
tally = 0
addednumbers = 0
switch = True
while switch == True:
    inputnumber = int(input("Enter a number: "))
    if inputnumber == 0:
        switch = False
    else:
        if inputnumber < 0:
            pass
        else:
            tally += inputnumber
            addednumbers += 1
print(f"You entered a total of {addednumbers} positive numbers with a sum of {tally}.")