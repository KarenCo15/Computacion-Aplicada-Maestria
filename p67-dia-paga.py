
dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
paga = [100,200,300,400,500,600,700]
pos = 0
dia = []

while True:
    dia = input("Dame un dia entre lunes y domingo: ")
    if dia in dias:
        break

print("Elegiste el dia:", dia)
pos = dias.index(dia)

print("La paga es: ", paga[pos])