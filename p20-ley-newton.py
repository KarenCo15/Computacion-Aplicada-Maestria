#Calula la segunda ley de newton(fuerza, masa y aceleración)

import os
os.system("cls")

print("Calula la segunda ley de newton(fuerza, masa y aceleración)\n")
print("[F] uerza      (f = m * a):")
print("[M] asa        (m = f / a):")
print("[A] celeración (a = f / m):")
op = input("Elige opción:").upper()

if op=="F":
    print("\nCalculando la Fuerza...")
    m=int(input("Dame la Masa: "))
    a=int(input("Dame la Aceleración: "))
    f = m * a
    print(f"\n La fuerza es {f}")
elif op=="M":
    print("\nCalculando la Masa...")
    f=int(input("Dame la Fuerza: "))
    a=int(input("Dame la Aceleración: "))
    m = f / a 
    print(f"\n La masa es {m}")
elif op=="A":
    print("C\nalculando la Aceleración...")
    f=int(input("Dame la Fuerza: "))
    m=int(input("Dame la Masa: "))
    a = f / m
    print(f"\n La Aceleración es {a}")
else:
    print("\nOpción iválida")

print("\n Proceso terminado...")
