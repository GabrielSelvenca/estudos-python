# Trocar os maiores valores da matriz por -1

import json

with open("matriz.json", "r") as arquivo:
    matriz = json.load(arquivo)
    
maior = 0
    
for x in range(len(matriz)):
    for y in range(len(matriz[x])):
        if matriz[x][y] > maior:
            maior = matriz[x][y]
            
for x in range(len(matriz)):
    for y in range(len(matriz[x])):
        if matriz[x][y] == maior:
            matriz[x][y] = -1
            
for l in matriz:
    print(l)