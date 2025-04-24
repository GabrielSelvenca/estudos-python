# Transformar uma matriz NxN em uma lista com todos os valores ordenados

import json

with open("matriz.json", "r") as arquivo:
    matriz = json.load(arquivo)
    
array = []

for x in range(len(matriz)):
    for y in range(len(matriz[x])):
        array.append(matriz[x][y])
        
print(array)