# Girar a matriz em 90 graus (sentido horário)

import json

with open("matriz.json", "r") as arquivo:
    matriz = json.load(arquivo)
    
nova_matriz = [[0 for _ in range(len(matriz))] for _ in range(len(matriz))]

for x, linha in enumerate(matriz):
    for y in range(len(matriz[x])):
        nova_matriz[y][len(matriz) - 1 - x] = linha[y]

for linha in nova_matriz:
    print(linha)