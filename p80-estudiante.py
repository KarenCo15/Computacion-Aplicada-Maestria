
estudiante = {
    "nombre":"Juan Perez",
    "edad":45,
    "email":"jperez@msn.com",
    "carrera":"Sistemas"
}

print (estudiante, len(estudiante), "\n")

estudiante["calificacion"] = 9.5

print (estudiante, len(estudiante), "\n")

estudiante["email"] = "juanp@gmail.com"

print (estudiante, len(estudiante), "\n")

estudiante.update({"sexo": "hombre", "semestre": 7})

print(estudiante, len(estudiante), "\n")
 
for k in estudiante.keys():
    print(k)
print()
for v in estudiante.values():
    print(v)
print()
for k,v in estudiante.items():
    print(k,v)

    
