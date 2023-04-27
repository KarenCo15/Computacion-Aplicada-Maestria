
notas= [ ]
n = 0
suma = 0
promedio = 0

print("Introduce notas entre 0 y 100  y usa 99 para terminar\n")

while n!=99:
    n=float(input("nota > "))
    if n>=0 and n<=100:
        notas.append(n)
        suma = suma + n
    else:
        print("x")

print("< Fin")

promedio = suma / len(notas)
print("Se capturaron:   ", len(notas))
print("Los notas son: ", notas)
print("\nEstadisticas")
print("Suma:     ", suma)
print("Promedio: ", promedio)
print("Nota maxima:    ", max(notas))
print("Nota minima:    ", min(notas))

mp = []
for n in notas:
    if n < promedio:
        mp.append(n)

print("Notas menores que el promedio:", len(mp))
print("Y son:", mp)



