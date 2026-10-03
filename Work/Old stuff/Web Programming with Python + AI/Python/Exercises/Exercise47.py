def evendigitcounter(number):
    tally = 0
    for i in range(len(str(number))):
        b = (number // 10**i) % 10
        if b % 2 == 0:
            tally += 1
    return tally
def odddigitcounter(number):
    tally = 0
    for i in range(len(str(number))):
        b = (number // 10**i) % 10
        if b % 2 != 0:
            tally += 1
    return tally

def divided(number):
    return evendigitcounter(number) / odddigitcounter(number)

print(divided(int(input("Enter a number: "))))