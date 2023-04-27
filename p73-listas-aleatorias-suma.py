import random

a = []
b = []
c = []

print("Generando listas de numeros aleatorios...")

for n in range(10):
    a.append(random.randint(1,100))
    b.append(random.randint(1,100))

print(f"La 1° lista de numeros aleatorios es {a} ")
print(f"La 2° lista de numeros aleatorios es {b} ")


print("Suma de ambas listas en una tercera, solo si los elementos son impares")
for n in range(10):
    if ((a[n]%2 !=0)) and ((b[n]%2 != 0)):
        elemento = a[n] + b[n]
        print(f"[{n+1}] {elemento}", end =" ")
        c.append(elemento)
    else:
        print (f"[{n+1}] !", end = " ")
    if(n !=9):
        print(f",", end =" ")

print("\n\nLista 3: ")
print(c)

print("\nLista 1: ")
print(a)
print("\nLista 2: ")
print(b)