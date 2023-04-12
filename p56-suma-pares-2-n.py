#Se desea imprimir los pares de 2 a n y su suma

n = int(input("Dame un numero:"))

s=0
print(f"\nNumeros pares de 2 a {n} y su suma")
for i in range (2,n+1,2):
    print(i,end = " ")
    s += i 
print("\nSuma de pares", s)

print("\nProceso terminado...")