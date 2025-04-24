# Trocar a diagonal principal pela diagonal secundária

import json

with open("matriz.json", "r") as arquivo:
    matriz = json.load(arquivo)
    
diagonal_principal = []
diagonal_secundaria = []

for i in range(len(matriz)):
    diagonal_principal.append(matriz[i][i])
    diagonal_secundaria.append(matriz[i][len(matriz) - 1 - i])

for i in range(len(matriz)):
    matriz[i][i] = diagonal_secundaria[i]
    matriz[i][len(matriz) - 1 -i] = diagonal_principal[i]

for linha in matriz:
    print(linha)