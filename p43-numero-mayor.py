#Calcular el número mayor de una serie de números introducidos por el usuario

import os 

while(True):
  
  os.system("cls")

  print("Calcular el número mayor de una serie de números introducidos por el usuario, salir con 0.\n")
  print("\nIntroducir numeros separados por un enter:")

  c= True
  b = 0

  while c == True:
   n = float(input())
   if b < n: 
      b = n
   if n == 0:
      print (f"El numero mayor es: {b}")
      c = False 
    
  res = input("\nDeseas continuar (S/N) ? ")
  if res.upper()=="N":
   break 
print("\nProceso terminado...")
