 #Calcular el volumen de un cilindro dado su radio y altura

import math

print("Calculando el volumen de un cilindro:\n")
Radio= int(input("Dame el radio de un cilindro:"))
Altura= int(input("Dame la altura de un cilindro:"))
Volumen = math.pi * (Radio * Radio) * Altura

print(f"El volumen del cilindro con radio de {Radio} y altura de {Altura} es {Volumen} ")
