# Calcular la temperatura convertida de grados centígrados a grados farenheit de un rango de valores introducidos por el usuario
import os 

while(True):
  
  os.system("cls")

  print("Calcular la temperatura convertida de grados centígrados a grados farenheit:\n")
  Inicial = int(input("Temperatura inicial: "))
  Final = int(input("Temperatura final: "))
  t = Inicial 
  print ("Tabla de temperaturas:")
  print(f"Centigrados (C)\t Farenheit (F) ")

  while t <= Final:
    print(f"\t{t} C\t\t  {float((t * 9 /5) + 32)} F")
    t += 1 

  res = input("\nDeseas continuar (S/N) ? ")
  if res.upper()=="N":
   break 
print("\nProceso terminado...")
