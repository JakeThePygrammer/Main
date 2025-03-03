listofnames = []
for index in range(6):
    listofnames.append(input("Enter a name : "))
prvi_dve = "#".join(listofnames[:2])
posledni_dve = "#".join(listofnames[4:])
print(prvi_dve)
print(posledni_dve)