#Imprimir pares e impares y su suma
import os

os.system("cls")
print("[P]ares de 1 a n y su suma\n[I]mpares y su suma")
op = input("Opcion: ").upper()
n = int(input("Hasta donde:"))

s=0
if op == "P":
    print(f"\nNumeros pares de 1 a {n} y su suma")
    for i in range (2,n+1,2):
        print(i,end = " ")
        s += i 
    print("\nSuma de pares", s)
elif op == "I":
    print(f"\nNumeros impares de 1 a {n} y su suma")
    for i in range (1,n+1,2):
        print(i,end = " ")
        s += i 
    print("\nSuma de impares", s)

print("\nProceso terminado")