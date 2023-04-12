#Acceder a una lista

nums = [10,20,30,40,60,70,10,20,99,100]

print(type(nums))
print(f"Tamaño de la lista {len(nums)}")
print(f"Todos los numeros de la lista {nums}")
print(f"El primero y el ultimo: {nums[0]},  {nums[-1]}")
print(f"DEl 30 al 70: {nums[2:6]}")
print(f"Tres primeros: {nums[:3]}")
print(f"Tres ultimos: {nums[7:]}")
