import numpy as np


lista = [1,2,3,4,5,6,7,7,8,6,9,12]
lista2 = [6,7,8,9,19]

print(lista)
#array unidimensional 
arr1 = np.array(lista)
arr2 = np.array(lista2)

# resultado = np.subtract(arr1,arr2)
# resultado2 = np.add(arr1,arr2)
# resultado3 = np.multiply(arr1,arr2)
# #resultado4 = np.(arr1,arr2)


# print(resultado)
# print(resultado2)
# print(resultado3)

#funciones estadisticas
media = np.mean(arr1)
mediana = np.median(arr1)
estandar = np.std(arr1)

print(media)
print(mediana)
print(estandar)
