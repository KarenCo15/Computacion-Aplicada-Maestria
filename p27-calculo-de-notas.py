#Calculando el promedio de 5 calificaciones y evaluando el resultado

import os
os.system("cls")

print("Calculando el promedio de 5 calificaciones:\n")
c1 = float(input("Calificacion 1: "))
c2 = float(input("Calificacion 2: "))
c3 = float(input("Calificacion 3: "))
c4 = float(input("Calificacion 4: "))
c5 = float(input("Calificacion 5: "))


suma = (c1 + c2 + c3 + c4 + c5) 
prom = suma / 5
print(f"\nTu promedio es {prom}")

if prom >0 and prom <=6:
    print("Quedas reprobado")
elif prom >6 and prom <=7:
    print("Pasas de panzaso")
elif prom >7 and prom  <=8:
    print("Muy bien,puedes mejorar")
elif prom >8 and prom  <=9:
    print("Excelente sigue asi")
elif prom >9 and prom  <=10:
    print("Perfecto tu esfuerzo valio la pena")
else:
    print("Completo")

print("\nProceso terminado")
