import pandas as pd 

# lista = [1,2,3,4,5,6,7,8,9,10]
# print(lista)

# #creaar una serie de pandas
# mi_serie = pd.Series(lista)
# print(mi_serie)


#crear un dataframe 
data = {
    'nombre':['ana','luis','carlos'], 'edad':[23, 24, 30], 'numero':[13131, 31314, 343141]
    }
df = pd.DataFrame(data['numero'])


print(df)