import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("poblacion.csv")
# print(df[["Date", "COL", "ARG"]])

# print(df.iloc[63])

# filtro = df[df['COL']>30000000]
# filtro1= filtro[['Date','COL']]
# print(filtro[['Date','COL']])
# print(filtro1)

# df = df.drop(columns=['ABW'])
print(df)
x = pd.array([2,4,9,16])
y = pd.array([1,2,3,4])

plt.plot(x,y )
plt.xlabel('Date')
plt.ylabel('Col')
plt.title('poblacion en colombia')
plt.show()