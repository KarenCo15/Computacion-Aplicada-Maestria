# Dados 3 números enteros (9,10,11) verificar si son consecutivos y mandar mensaje confirmándolo, si no lo son (1,4,6) mandar mensaje de error.

import os
os.system("cls")

print("Dado 3 numeros enteros verificar si son consecutivos\n")
print("Dame 3 numeros enteros separados por un espacio:")
n1,n2,n3 =input().split()
n1,n2,n3 =[int(n1),int(n2),int(n3)]

if n1==9 and n2== 10 and n3== 11:
    print(f"{n1},{n2},{n3} son numeros consecutivos")

else:
    print(f"{n1},{n2},{n3} no son numeros consecutivos")


print("\n Proceso terminado")
