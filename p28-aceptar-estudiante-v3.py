#Aceptar un estudiante en base a su sexo, edad y sus calificaicones

import os
os.system("cls")

print("Aceptar un estudiante en base a su sexo, su edad y sus calificaicones\n")
sexo = (input("Indica tu sexo siendo [F]emenino y [M]asculino:\n")).upper()


if sexo == "F":
    nombre = input("Dame tu nombre: ")
    edad= int(input("Dame tu edad:"))
    if edad > 21:
       print("Dame tres calificaciones separadas por enter: ")
       c1,c2,c3 = int(input()), int(input()), int(input())
       prom = (c1 + c2 + c3)/3
       print(f"Tu promedio es: {prom}")
       if prom >=8 and prom <=9.5:
        print(f"{nombre} bienvenido(a) a la universidad, tu edad  {edad} y tu promedio {prom} lo permiten")
       else:
        print("No aceptamos un promedio menor a 8")
    else:
        print("No aceptamos menores de 21")

else:
    print("No aceptamos hombres...")

print("\n Proceso terminado")


