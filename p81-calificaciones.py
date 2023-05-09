
materias = ["fisica","quimica","matematicas","geografia","estadistica"]
califs   = [10, 9, 8, 7.5, 6]

notas = dict( zip(materias,califs) )

print(notas, len(notas), "\n")

notas.update({"ingles": 10, "programacion": 7})
print(notas, len(notas), "\n")

notas.pop("fisica")
print(notas, len(notas), "\n")

notas.popitem()
print(notas, len(notas), "\n")

notas.update({"quimica":10, "matematicas":10})
print(notas, len(notas), "\n")

s = 0
print("materia  calificacion")
for m,c in notas.items():
    print(f"{m:<12}- {c:5}")
    s = s + c 

print()
print (s)
print (s/ len(notas))


