nameslist = []
nameslen = []

for index in range(5):
    name = input("Enter a name: ")
    nameslist.append(name)
    nameslen.append(len(name))

print(f"Names in list: {nameslist}")
print(f"Lengths of names in list: {nameslen}")