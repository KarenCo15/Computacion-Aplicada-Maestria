import random

a = []
b = []
c = []

print("Generando listas de numeros aleatorios...")

for n in range(10):
    a.append(random.randint(5,10))
    b.append(random.randint(5,10))

print(a)
print(b)

for n in range(10):
    a[n] = a[n] * a[n]
    b[n] = b[n] * b[n]

print(a)
print(b)

for n in range(10):
    c.append(a[n] + b[n])
print(c)
