#Iterar sobre los elementos de una lista
nums = [2,4,6,8,10,12,14,16]

print(f"Todos los elementos :\n {nums}")

print("\nIterar por los elementos de la lista forma 1:")
for n in nums:
    print (n, end= " ")

print("\nIterar por los elementos de la lista forma 2:")
for i in range(len(nums)):
    print (nums[i],end= " ")

print("\nMostrar cada elemento de la lista sumado en 2:")
for n in nums:
    print (n+2, end= " ")
print(f"\n{nums}")

print ("\nModificar la lista sumando 10 a cada elemento:")
for i in range(len(nums)):
    nums[i] = nums[i] + 10
print (f"\n{nums}")