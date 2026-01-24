list1 = []
abc = int(input("How many numbers do you want to enter: "))
for index in range(abc):
    a = int(input("Enter a number: "))
    list1.append(a)
even = 0
odd = 0
for element in list1:
    if element % 2 == 0:
        even +=1
    else:
        odd +=1
print(f"There are {even} even numbers in the list that you entered")
print(f"There are {odd} odd numbers in the list that you entered")
