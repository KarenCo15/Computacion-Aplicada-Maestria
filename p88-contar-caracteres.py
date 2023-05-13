
caracter= {}
palabra = input("Escribe una palabra para contar caracteres: ")

for i in palabra:
    if i in caracter:
        caracter[i] = 1 + caracter[i]
    else:
        caracter[i] = 1

print(f"{caracter}")
