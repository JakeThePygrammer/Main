def even_numbers(list1):
    count = 0
    for i in list1:
        if i % 2 == 0:
            count += 1
    return count

def odd_numbers(list1):
    count = 0
    for i in list1:
        if i % 2 != 0:
            count += 1
    return count

list1 = []
for i in range(10):
    list1.append(int(input("Enter a number: ")))

print(f"The number of odd numbers is {odd_numbers(list1)}, and the number of even numbers is {even_numbers(list1)}")