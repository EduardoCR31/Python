# redes = {

# }
# for i in range(3):
#     red = input("Nombre de la red: ")
#     clave = input("contrasena: ")
#     redes[red]=clave
# print(redes)

redes = [] 
while True:
    print("opcion 1 añadir redes, opcion 2 ver redes")
    opcion = int(input("ingrese una opcion"))
    if opcion == 1:
        red = {}
        print("ingrese la red")
        nombre = input()
        red["nombre"] = nombre 
        clave = input()
        red["clave"] = clave
        redes.append(red)
    elif opcion == 2:
        for i in range(len(redes)):
            print(redes[i])
            