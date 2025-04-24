# Somar os elementos da diagonal principal de uma matriz

import json

with open("matriz.json", "r") as arquivo:
    matriz = json.load(arquivo)
    
soma = 0

for i in range(len(matriz)):
    soma += matriz[i][i]
    
print(f"Soma da diagonal da matriz: {soma}")