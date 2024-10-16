import random

maquina = random.choices([1, 2, 3])
print("1 piedra, 2 tijera, 3 papel")

jugador = int(input())
print(maquina)
if jugador == 1 and  maquina == 2:
    print("ganaste")
elif jugador == 2 and maquina == 3:
    print("ganaste")
elif jugador == 3 and maquina == 1:
    print("ganaste")
elif jugador == maquina:
    print("empate")
else:
    print("perdiste")
        