import string, random
def passwordcreator():
    lowercaseletters = string.ascii_lowercase
    uppercaseletters = string.ascii_uppercase

    listpass = [random.choice(lowercaseletters),random.choice(lowercaseletters), random.choice(lowercaseletters)
        ,random.choice(uppercaseletters), random.choice(uppercaseletters), str(random.randrange(0, 10)),
    str(random.randrange(0, 10)), random.choice(["!", ",", ".", "_", "[", "]", "@", "#", "$", "%", "^", "&", "*"]),
    random.choice(["!", ",", ".", "_", "[", "]", "@", "#", "$", "%", "^", "&", "*"])]

    random.shuffle(listpass)
    listpassstr = listpass[0] + listpass[1] + listpass[2] + listpass[3] + listpass[4] + listpass[5] + listpass[6] + listpass[7] + listpass[8]
    return listpassstr

print(passwordcreator())