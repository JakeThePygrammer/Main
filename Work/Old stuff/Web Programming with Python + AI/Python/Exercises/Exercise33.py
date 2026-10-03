listnames = []
switch = True
while switch == True:
    name = input("Enter a name or 'stop' to stop: ")
    if name == "stop":
        switch = False
    else:
        listnames.append(name)
print(f"You entered {len(listnames)} names, they are: {listnames}.")