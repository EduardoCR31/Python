#bucle while

listatamano = input("rango de la lista: ")
# i = 1
# lista = []
# while i <= int(listatamano):
    
#     numero = input (f"ingrese el numero {i}: ")
#     lista.append(int(numero))
#     i += 1
# print("la lsita ingresada: ", lista)
# lista.sort()
# print("la lista ordenada:", lista)


lista = []
tamano = 0
while tamano != 0:
    numerolista = input (f"ingrese numero {tamano}:")
    lista.append(int(numerolista))
    tamano -= 1

print(lista)   