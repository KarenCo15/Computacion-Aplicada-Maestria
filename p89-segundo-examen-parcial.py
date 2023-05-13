
empleados= []

print("Muebleria Muebles Dico")
print("Sistema de Procesamiento de Empledos")
print("Captura de datos de los empleados, * para terminar:")

while True:
    empleado= {}
    nombre= input("\nNombre\t\t: ")
    if nombre == ""or nombre == "*":
        break
    else:
        empleado["nombre"] = nombre
        empleado["edad"] = int(input("edad\t\t: "))

        while True:
            sexo = input("sexo (h/m)\t: ").upper()
            if sexo == "H" or sexo == "M":
                empleado["sexo (h/m)"] = sexo
                break
            else:
                print("\nError")

        empleado["sueldo"]= int(input("sueldo\t\t: "))
        empleados.append(empleado)


print("\nLos datos como se guardan:")
print(" ")
print(empleados)
print("\nTabla de datos:")
print("Nombre\tEdad\tSexo\tSalario")

for empleado in empleados:
    for i in empleado.keys():
        if i != "sueldo":
            print(f"{empleado[i]}\t", end= " ")
        else:
            print(f"{format(empleado[i])}\t", end= " ")
    print("\r")

sumam = 0
for j in empleados:
    if j["sexo (h/m)"] == "m" or j["sexo (h/m)"] == "M":
        sumam = sumam + 1

sumah = 0
for k in empleados:
    if k["sexo (h/m)"] == "h" or k["sexo (h/m)"] == "H":
        sumah = sumah + 1

sumae = 0
promedioe = 0
for n in empleados:
    sumae = sumae + n["edad"]
promedioe = sumae/len(empleados)

sumasu = 0
promediosu = 0
for l in empleados:
    sumasu = sumasu + l["sueldo"]
promediosu = sumasu/len(empleados)

print("\nResumen :")
print(f"Empleados: {len(empleados)}")
print(f"Mujeres  : {sumam}")
print(f"Hombres  : {sumah}")
print(f"Edad     : suma:\t{sumae},\t\tpromedio: \t{promedioe}")
print(f"Sueldo   : suma:\t{format(sumasu)}\tpromedio:\t{format(promediosu)}")
