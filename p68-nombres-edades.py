
nombres = []
edades = []
pos = 0
mayor = 0

print("Introduce nombres y edades, * para terminar:\n")

while True:
    nombre= input("nombre: ")
    if nombre == "*":
        break
    else:
        nombres.append(nombre)
        edad = int(input("edad: "))
        edades.append(edad)

print(nombres)
print(edades)


for i in range(len(nombres)):
    if edades[i] >= 18:
        print(f"nombre: {nombres[i]}, edad: {edades[i]}")

may = max(edades)
pos = edades.index(may)

print("La persona de mayor edad es:")
print(f"nombre: {nombres[pos]}, edad: {edades[pos]}")
