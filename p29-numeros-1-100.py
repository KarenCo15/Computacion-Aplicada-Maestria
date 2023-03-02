#Imprime numeros del 1 al 100 

import os 
os.system("cls")

print("Imprimir numeros del 1 al 100:\n")
n = (int(input("Hasta donde:")))
m = (int(input("salto:")))

c = 1
while c <= n:
    print(c, end = " ")
    c= c + m

print("\nProceso terminado...")
