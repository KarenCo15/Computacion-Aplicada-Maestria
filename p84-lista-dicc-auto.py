
autos = [
    { 'marca':'Ford', 'modelo':'Mustang',  'ano':1964 },
    { 'marca':'VW', 'modelo':'Jetta',  'ano':2015 }
]

autos.append({"marca": "Ford","modelo": "focus",  "año":2000})

print(autos, len(autos))

for auto in autos:
    print(auto)

print("\nDatos en forma de tabla")
for k in autos[0].keys():
    print(f"{k}\t", end =" ")
print("\r")

for auto in autos:
    for v in auto.values():
        print(f"{v}\t",  end=" ")
    print("\r")

print("\nDatos en forma de registro: ")
for auto in autos:
    for k,v in auto.items():
        print(f"{k} - {v}")
    print("\r")