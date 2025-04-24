# Criar uma nova matriz onde cada célula seja a média dos seus vizinhos

import json

with open("matriz.json", "r") as arquivo:
    matriz = json.load(arquivo)
    
nova_matriz = [[0 for _ in range(len(matriz))] for _ in range(len(matriz))]
vizinhos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        soma = 0
        count = 0
        for dx, dy in vizinhos:
            x = i + dx
            y = j + dy
            if (0 <= x < len(matriz) and 0 <= y < len(matriz[0])):
                soma += matriz[x][y]
                count+=1
        media = soma / count if count > 0 else 0
        nova_matriz[i][j] = media

for l in nova_matriz:
    print(l)