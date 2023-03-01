# Dado un numero entero entre 1 y 7, mostrar el dia de la semana correspondiente
# 1=domingo, 2=lunes, 3=martes.....

import os
os.system("cls")

print("Muestra el dia de la semana:\n")
numero= int(input("Dame un númer entre 1 y 7 : "))

if numero >= 1 and numero <= 7:
    print(f"El dia de la semana es  " , end= '')
    if numero == 1 :
        print("Domingo")
    elif numero == 2:
        print("Lunes")
    elif numero == 3:
        print("Martes")
    elif numero == 4:
        print("Miercoles")
    elif numero == 5:
        print("Jueves")
    elif numero == 6:
        print("Viernes")
    elif numero == 7:
        print("Sabado")
    else:
        print("completo")

else:
    print("el numero esta fuera de rango...")

print("\n Proceso terminado")
