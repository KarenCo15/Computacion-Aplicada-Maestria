#Verifica si un número es positivo, negativo o cero

import os
os. system("cls")
print("Verifica si un número es positivo,negativo o cero\n")
numero = int(input("Dame un número?"))

if numero > 0:
    print("El numero es POSITIVO")

if numero < 0:
    print("El numero es NEGATIVO")

if numero == 0:
    print("El numero es CERO")

print("\nProceso Terminado...")
