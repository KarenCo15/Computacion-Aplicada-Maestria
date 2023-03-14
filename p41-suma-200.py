#Introducir numeros hasta que la suma de estos de 200 (break) y mostrar cuantos numeros se introdujeron y la suma de estos 
import os 

while(True):
  
  os.system("cls")
  print("Introducir numeros hasta que la suma de estos de 200 (break)")
  suma = 0
  cuenta = 0
  
  
  while (True):
   num = float(input("Numero:"))
   if num <= 200:
     suma = suma + num
     cuenta = cuenta + 1
   if suma >= 200 :
     break

  print (f"\nSe introdujeron {cuenta} numeros ")
  print(f"\nLa suma de los numeros es: {suma}")

  res = input("\nDeseas continuar (S/N) ? ")
  if res.upper()=="N":
   break 
print("\nProceso terminado...")

