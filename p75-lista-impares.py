

#Pedir un elemento a buscar en la lista original y decir si esta y en que posición
impares = []
numerosdiv = []
numerosim = 0
suma = 0
suma2 = 0

n = int(input("Cuantos numeros impares?"))

while len(impares) != n:
    numerosim = numerosim + 1
    if (numerosim%2 != 0):
        impares.append(numerosim)
        suma = suma + numerosim
print (impares)
promedio = suma / len(impares)
print(f"\nSuma: {suma}")
print(f"Promedio: {promedio}")

for i in impares:
    if (i%3 == 0):
        numerosdiv.append(i)
        suma2 = suma2 + i

while True:
    buscar = int(input("\nElemento a buscar en la lista original y salir con 0:  "))
    if buscar in impares:
        print (f"El numero {buscar} esta en la posicion {impares.index(buscar)} de la lista original")
    elif (buscar == 0):
        break
    else:
        print("No esta en la lista")




