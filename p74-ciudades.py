


ciudades = [ ]
consonantes = ["b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","x","z","w","y" ]
iniciales = [ ]

print("Leer n nombres de ciudades en una lista hasta introducir $")

while True:
    ciudad= input("Ciudad: ")
    if ciudad == "$":
        break
    else:
        ciudades.append(ciudad)
        
print("Se capturaron:   ", len(ciudades))
print("Las ciudades son: ", ciudades)
print("\nOrdenadas (sort): ")
ciudades.sort()
print(ciudades)
print("En orden descendente:")
ciudades.sort(reverse=True)
print(ciudades)

for isConsonante in ciudades:

    if(isConsonante.lower().startswith(tuple(consonantes))):
        iniciales.append(isConsonante)

print(f"\nCiudades que inician con consonantes son: {len(iniciales)}")
print(f"{iniciales}")

