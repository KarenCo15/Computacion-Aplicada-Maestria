dias = {1:"Lunes",2:"Martes",3:"Miercoles",4:"Jueves",5:"Viernes",6:"Sabado",7:"Domingo"}


while True:
    numeros= int(input("Dame un numero de dia de la semana: "))
    if numeros > 0 and numeros < 8:
        print(f"El dia de la semana es: {dias[numeros]}")
        break
    else:
        print("Error")
