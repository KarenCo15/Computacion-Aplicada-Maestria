
a = []
b = []
c = []

n = int(input("Cuantos elementos: "))

print("Dame los elementos de la primera lista: ")
for i in range(n):
    x = int(input(f"Lista 1 elemento {i}: "))
    a.append(x)
print(a)

print("Dame los elementos de la segunda lista: ")
for i in range(n):
    x = int(input(f"Lista 1 elemento {i}: "))
    b.append(x)
print(b)

print("Calculando la multiplicacion de la lista 1 por la lista 2")
for i in range(n):
    x = a[i] * b[i]
    c.append(x)
print(c)

print("\nLas tres listas son:")
print (a,b,c)