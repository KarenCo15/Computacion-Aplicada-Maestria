#Imprime numeros pares de forma descendente desde 100 hasta donde el usuario diga

import os 

while(True):
  
  os.system("cls")

  print("Imprime numeros pares de forma descendente:\n")
  n = int(input("Los numeros pares desde donde:"))
  m = int(input("Hasta donde:"))
  c = suma = 0
  
  c = n
  while c > 0:
    c= c - 1
    if c % 2 == 0:
     print(c, end = " ")
     suma = suma + c
   
  print (f"\nLa suma de los numeros es: {suma}")

  res = input("\nDeseas continuar (S/N) ? ")
  if res.upper()=="N":
     break

print("\nProceso terminado...")


