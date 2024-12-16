lista_na_broevi = []
def suma(lista):
    """This function is used to add all the numbers from the list together."""
    suma = 0
    for number in lista:
        suma += number
    return suma
for index in range(10):
    lista_na_broevi.append(int(input("Enter a number ")))
print(suma(lista_na_broevi))
print(suma.__doc__)