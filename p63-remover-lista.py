#Remover elementos de una lista
nums = [1,3,5,7,9,11,99,15,88,19,100]
print (f"Todos los numeros: \n {nums} - {len(nums)}")
nums.remove(99)
print(f"Remover primera ocurrencia\n {nums} - {len(nums)}")
num = nums.pop(8)
print (f"Remover elemento en una posicion\n {nums} - {num} - {len(nums)}")
num = nums.pop()
print (f"Remover elemento en una posicion\n {nums} - {num} - {len(nums)}")
nums.clear()
print (f"Remover todos: \n {nums} - {len(nums)}")