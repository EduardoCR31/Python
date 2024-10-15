#bucle for
listatamano = input("rango de la lista: ")
lista = []
for i in range (int(listatamano)):
    numero = input (f"ingrese el numero {i}: ")
    
    lista.append(int(numero))
print("la lsita ingresada: ", lista)
lista.sort()
print("la lista ordenada:", lista)



# bucle while
 