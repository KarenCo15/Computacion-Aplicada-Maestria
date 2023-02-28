#Verifica si la suma de dos numeros es igual a un tercero
# ni=4, n2=5, n3=9      n1+n2=n3    n2+n3=n1    n1+n3=n2

import os
os.system("cls")

print("verifica si la suma de dos numeros es igual a un tercero\n")
print("Dame 3 numeros enteros separados por un espacio:")
n1,n2,n3 =input().split()
n1,n2,n3 =[int(n1),int(n2),int(n3)]

if n1+n2 == n3:
    print("n1 + n2 = n3")
elif n2+n3 == n1:
    print("n2 + n3 = n1")
elif n1+n3 == n2:
    print("n1 + n3 = n2")
else:
    print("no hay sumas factibles")

print("\n Proceso terminado")