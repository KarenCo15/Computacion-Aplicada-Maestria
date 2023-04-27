
mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias = [31,28,31,30,31,30,31,30,31,30,31,30]
pos = 0

while True:
    pos = int(input("Dime un mes entre 1 y 12: "))
    if pos >= 1 and pos <= 12:
        break
    else:
        print("no es un mes")

print(f"El mes que elegiste es: ({mes[pos-1]}, {dias[pos-1]} dias)")
