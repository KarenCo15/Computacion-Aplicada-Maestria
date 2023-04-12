#Se desea imprimir la secuencia de términos armónicos el numero de renglones que el usuario desee y su suma:

import os
os.system("cls")

n = int(input("¿Cuantos terminos? "))
m= 0


for i in range(1,n+1):
    print (f"1/{i}! + ", end= " ")
    m += (1/i)

print("\nLa suma es: ", m)
print("\nProceso terminado...")