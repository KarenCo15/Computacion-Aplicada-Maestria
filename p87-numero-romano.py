
numeros= {
    1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",10:"X",
    11:"XI",12:"XII",13:"XIII",14:"XIV",15:"XV",16:"XVI",17:"XVII",18:"XVIII",19:"XIX",20:"XX"
    }

while True:
    numero= int(input("Dame un numero en arabigo del 1 al 20: "))
    if numero > 0 and numero < 21:
        print(f"El equivalente en numero romano es : {numeros[numero]}")
        break
    else:
        print("Error")