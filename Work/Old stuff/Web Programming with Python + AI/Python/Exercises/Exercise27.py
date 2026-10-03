list50 = []
list3 = []

for index in range(1,51):
    list50.append(index)

for element in list50:
    if element % 3 == 0:
        list3.append(element)
print(list3)