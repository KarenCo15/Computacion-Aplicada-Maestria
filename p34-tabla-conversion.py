# Imprimir una tabla de conversion de peso a dolar
import os

while(True):

  os.system("cls")
  tc = 18.00

  pi = float(input("Valor inicial:"))
  pf= float(input("Valor final:"))

  c= pi 

  print("\nPesos\tDolar")
  print("_"*15)

  while c <= pf:
    print(f'{c}\t{c/tc:.4f}')
    c += 1

  print("_"*15)


  res = input("\nDeseas continuar (s/N) ?")
  if res.upper()=="N":
    break
 
