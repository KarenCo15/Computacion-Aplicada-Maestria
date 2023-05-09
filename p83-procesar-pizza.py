
base = 15
subtotal = 0
total = 0

ingredientes = {"T":1.50, "P":3.50, "C":3.74, "A":0.40, "Q":4.0}
pedido = input("Ingredientes de la pizza: ").upper()
for i in pedido: 
    if i in "TPCAQ":
        subtotal= subtotal + ingredientes[i]

subtotal = subtotal + base

if subtotal >= 20:
    total = subtotal - (subtotal*0.05)

print(f"El subtotal es: {subtotal}")
print(f"El total es: {total}")
