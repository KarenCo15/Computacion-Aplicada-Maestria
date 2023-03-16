#Imprimir numeros de 1 a n o de n a 1 segun decida el usuario

import os
while True:
 os.system ("cls")

 print("[1] Numeros de 1 a n ")
 print("[2] Numeros de n a 1 ")
 op = int(input("Elige: "))
 n  = int(input("Limite n: "))

 if op == 1:
    print (f"\nImprimiendo numeros de 1 a {n}")
    for v in range (1,n+1):
        print (v,end= " ")

 if op == 2:
    print (f"\nImprimiendo numeros de {n} a 1")
    for r in range (n,0,-1):
        print (r,end= " ")

 else:
    print("\nOpcion invalida")

 res = input("\nDeseas continuar (S/N) ? ")
 if res.upper()=="N":
   break 

print("\n\nProceso terminado...")
