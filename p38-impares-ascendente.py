#Imprime numeros impares de forma ascendente desde 1 hasta el numero que el usuario decida

import os 

while(True):
  
  os.system("cls")

  print("Imprime numeros impares de forma ascendente:\n")
  n = (int(input("Hasta donde:")))
  c= suma = 0


  while c < n:
    c= c + 1
    if c % 2 != 0:
     print(c, end = " ")
     suma = suma + c
    if c >= n:
        print (f"\nLa suma de los numeros es: {suma}")

  res = input("\nDeseas continuar (S/N) ? ")
  if res.upper()=="N":
     break

print("\nProceso terminado...")
