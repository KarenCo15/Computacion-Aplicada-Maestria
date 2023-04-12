#Cambiar una lista

calif = [10,9,8.5,6.5,9.8,7,5,6.2,9.5]

print(f"Todas las calificaciones: \n {calif} - {len(calif)}")
calif[0] = 7
calif[1] = 7
print(f"Modificar elemento 0 y elemento 1: \n {calif}")
calif[2:5] = [9,9,9]
print (f"Modificar de 2:5 - : \n {calif}")