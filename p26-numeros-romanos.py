#Dado un numero del 1 al 10 mostrar su equivalente en numeros romanos 

import os
os.system("cls")

print("Dado un numero del 1 al 10 mostrar su equivalente en numeros romanos:\n")
numero= int(input("Dame un númer entre 1 y 10 : "))

if numero >= 1 and numero <= 10:
    print(f"Su equivalente en numero romano es  " , end= '')
    if numero == 1 :
        print("I")
    elif numero == 2:
        print("II")
    elif numero == 3:
        print("III")
    elif numero == 4:
        print("IV")
    elif numero == 5:
        print("V")
    elif numero == 6:
        print("VI")
    elif numero == 7:
        print("VII")
    elif numero == 8:
        print("VIII")
    elif numero == 9:
        print("IX")
    elif numero == 10:
        print("X")

    else:
        print("completo")

else:
    print("el numero esta fuera de rango...")

print("\n Proceso terminado")
