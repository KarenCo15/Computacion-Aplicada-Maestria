#Dados dos ángulos de un triángulo, calcular el 3er ángulo
 
print("Claculando el tercer ángulo de un triángulo:\n")
ángulo1 = int(input("Dame el ángulo 1:"))
ángulo2 = int(input("Dame el ángulo 2:"))

ángulo3 = 180 - (ángulo1 + ángulo2)
print(f"El ángulo 3 = {ángulo3}")
