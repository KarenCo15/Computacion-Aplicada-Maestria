#Examen Parcial 1
#Se desea llevar el control de la inscripción a un evento académico de la Universidad Patito. Se especifica: Tipo de usuario, paquete y cantidad.

import os 
it= float(0) 

while(True):
  
  os.system("cls")



  print("Universidad Patio SA de CV \nSistema de Inscripción Congreso de Sistemas")

  tu= int(input ("\nIndica el tipo de usuario: [1] Alumno $100, [2] Trabajador $200, [3] Docente $500 : " ))
  if  tu == "1":
   u= "alumno"
   p=100
   des =20   
  elif tu == "2":
   u = "Trabajador"
   p=200
   des =10
  else: 
   u = "Docente"
   p =500
   des =5
   
  tp= int(input("Indica el tipo de paquete: [1] Solo conferencias $600, [2] Con eventos sociales $800, [3] Con kit de acceso $900  :"))

  if tp == "1":
   pa= "Conferencias"
   pp =600

  elif tp == "2":
   pa = "Eventos sociales"
   pp =800

  else:
   pa = "Kit de acceso"
   pp =900

  c= int(input("Cantidad que requiere : "))
  sub = (p + pp) * c
  descuento = float(sub * des)/100
  total = float(sub - des)

  it= it + total 

  print (f"\nResumen del pedido: \nTu pedido fue una cantidad de: {c} paquetes,  del tipo de usuario: {u} y del tipo de paquete: {pa} ")
  print (f"El subtotal de tu pedido: ${sub}  con un descuento de: ${descuento}{des} Dejando un total de: ${total} ")


  x = True
  while (x==1):
      print("\nDeseas continuar (S/N) ? ", end = " " )
      res = input()
      if res.upper()=="S" or res.upper() == "N":
          x = False 
  if res.upper() == "N":
    break 
  
print(f"\nImporte total de la venta: ${it}")

print("\nProceso terminado...")

