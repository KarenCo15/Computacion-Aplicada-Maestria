#Imprime la tabla de multiplicar que el usuario pida 

import os 
os.system("cls")

while True:

    t=int(input("Que tabla quieres : "))
    n=int(input("Hasta donde : "))

    for i in range (1,n+1):
        print (f"{t} x {i} = {t*i}")

    res = input("Deseas continuar (S/N) ?") .upper()
    if res=="N":
        break
print("\nProeso terminado...")