cliente = {
    "nombre":"jorge",
    "apellido":"rodriguez",
    "telefono": "3236311234",
    "saldo": "50000",
    "edad": "40"
}
print(cliente)
valor = cliente.get("nombre")
print(valor)
cliente["profesion"]="ingeniero" #agrega atributos nuevos al diccionario
print(cliente)
print(cliente["telefono"])

del cliente["edad"] #eliminar atributos del diccionario
print(cliente)

cliente["Estado laboral"]="desempleado"
print(cliente)
claves = cliente.keys()
print(claves)

valores = cliente.values()
print(valores)

