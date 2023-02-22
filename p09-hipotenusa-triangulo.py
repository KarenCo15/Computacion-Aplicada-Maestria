#Calcular la hipotenusa de un triángulo rectángulo

import math
print("Calcular la hipotenusa de un triángulo rectángulo dadas las longitudes de sus lados:\n")
longlado1 = int(input("Dame la longitud del lado 1:"))
longlado2 = int(input("Dame la longitud del lado 2:"))

hipotenusa = math.sqrt( longlado1 * longlado1 + longlado2 * longlado2 )
print(f"La hipotenusa es:, {hipotenusa}")
