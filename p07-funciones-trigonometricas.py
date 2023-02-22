# Uso de las funciones trigonométricas básicas de un ángulo en radianes

import math
import os

os.system("cls")
print("Calcula las funciones trigonométricas básicas de un ángulo en radianes:\n")
angulo= int(input("Dame un angulo en radianes : "))

seno = math.sin(angulo)
cos  = math.cos(angulo)
tan  = math.tan(angulo)
grados = math.degrees(angulo)

salida=("Resumen de funciones trigonométricas\n"
f"El seno es: {seno}\n"
f"El coseno es: {cos}\n"
f"La tangente es: {tan}\n"
f"El angulo {angulo} en radianes equivale a {grados}\n")

print(salida)