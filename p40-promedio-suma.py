#calcular la suma y el promedio de una serie de números introducidos por el usuario hasta salir con  0 y calcular su suma

import os 

while(True):
  
 os.system("cls")

 print("Calculando la suma y el promedio de una serie de numeros hasta salir con 0\n")

 suma  = 0
 cuenta = 0

 n = 1
 while n > 0:
  n = float(input("Numero:"))
  if n != 0:
   cuenta = cuenta + 1
   suma = suma + n
  
 
 print(f"\nLa suma es    : {suma}")
 print(f"El promedio es: {suma/cuenta}\n")

 res = input("\nDeseas continuar (S/N) ? ")
 if res.upper()=="N":
     break 
print("\nProceso terminado...")