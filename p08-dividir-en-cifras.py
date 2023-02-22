# Dividir un número en 3 cifras, en centenas, decenas y unidades
#971 9 centenas 7 decenas 1 unidad

import os
os.system("cls")

print("Dividir un número de 3 cifras en centenas, decenas y unidades:\n")
num= int(input("Dame un número de 3 cifras: "))

centenas = num//100
decenas = (num- (centenas*100))//10
unidades = num -centenas*100 - decenas*10

print("centenas", centenas)
print("decenas", decenas)
print("unidades", unidades)
