#Se desea imprimir los numeros de 1 a n de 10 en 10

import os
os.system ("cls")

n = int(input("Dame un numero: "))


for x in range(1,n+1,10): 
    print (x,end = " ")


print("\nProceso terminado...")