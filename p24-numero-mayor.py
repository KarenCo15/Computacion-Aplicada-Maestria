# Dados tres números enteros, verificar cual es el mayor.

import os
os.system("cls")

print("Dado 3 numeros enteros verificar cual es el mayor \n")
print("Dame 3 numeros enteros separados por un espacio:")
n1,n2,n3 =input().split()
n1,n2,n3 =[int(n1),int(n2),int(n3)]

if n1 > n2 and n1 > n3:
    print(f"{n1} es el numero mayor")
elif n2 > n1 and n2 > n3:
    print(f"{n2} es el numero mayor")
else:
    print(f"{n3} es el numero mayor")



print("\n Proceso terminado")
