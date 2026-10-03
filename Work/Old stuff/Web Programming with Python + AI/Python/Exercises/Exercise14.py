nameslist = []

for index in range(5):
    name = input("Enter a name: ")
    nameslist.append(name)

print(f"Names in list: {nameslist}")
print(f"First name in list: {nameslist[0]}, last name in list: {nameslist[-1]}")
print(f"List length: {len(nameslist)}")