
A = {50,60,70,80,90,100,200}
B = {60,90,100,300,400,500}
C = {10,20,60,90,70,100,600,700}
print(f"\nA= {A}, B= {B}, C= {C}")

print("\nLa union de los conjuntos A y B es:")
print(A|B, "\n")
print("\nLa union de los conjuntos B y C es:")
print(B|C, "\n")

print("\nLa diferencia de los conjuntos A y C es:")
print(A - C, "\n")

print("\nLa diferencia simetrica de los conjuntos B y C es:")
print(B ^ C, "\n")

print("\nLa interseccion de los conjuntos B y C es:")
print(B & C, "\n" )

print( A.issubset(B),"\n")
print(C <= A, "\n")

print(100 in A, "\n")
print(60 in A, "\n")
print(60 in B, "\n")
print(60 in C, "\n")
print(900 not in C, "\n")

