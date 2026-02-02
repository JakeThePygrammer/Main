counter = 1

while True:
    a = counter
    while a not in (1, 2, 4):
        if a % 2 == 0:
            a //= 2
        else:
            a = 3 * a + 1

    print(f"{counter} = False")
    counter += 1

#Infinite loop, leave running while zzz.