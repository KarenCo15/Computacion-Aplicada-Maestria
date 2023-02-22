#Convirtiendo un numero dado en  horas en dias, minutos y segundos

print("Convertir un número dado en horas en dias, minutos y segundos:\n")
horas= int(input ("Dame un numero de horas:"))

numero = horas
dias     = horas // 24
minutos  = horas * 60
segundos = minutos * 60

print(dias, "dias")
print(minutos, "minutos")
print(segundos, "segundos")
