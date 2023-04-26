
A = {"Juan", "Maria", "Pedro", "Jose", "Rocio"}
B = {"Pedro", "Juan", "Pablo", "Mateo", "Esther"}


print(f"\nA= {A}, B= {B},")

print("\nLa union de los conjuntos A y B es:")
print(A|B, "\n")

print("\nLa interseccion de los conjuntos A y B es:")
print(A & B, "\n" )

print("\nLa diferencia de los conjuntos A y B es:")
print(A - B, "\n")

print("\nLa diferencia simetrica de los conjuntos A y B es:")
print(A ^ B, "\n")

C= ("Pablo", "Mateo")
print(B.issubset(C),"\n")

D=("Reynaldo","Angelica")
print(A.issuperset(D), "\n")

print("Pedro" in A, "\n")
print("Lilia" not in B, "\n")
