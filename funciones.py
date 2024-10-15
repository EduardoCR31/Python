
def calculopro (x,y):
    return x * y

cantidadpro = 1  
totalcompra = 0
    
while cantidadpro != 0:
    cantidadpro = float(input("cantidad producto: "))
    if cantidadpro == 0:
        break
    valorpro = float(input("valor producto: "))
    subtotal = calculopro(cantidadpro, valorpro)
    print ("la cantidad es: ", cantidadpro)
    print ("el valor del producto es :", valorpro)
    print ("el subtotal del producto es :", subtotal)
    totalcompra += subtotal

print (f"el total de los productos es {totalcompra}")
 
    
    
    
        
    
    



# total = 1
# print(f"el total de los productos es {total}")
