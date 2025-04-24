# Identificar a linha com maior soma

import json

with open("matriz.json", "r") as arquivo:
    matriz = json.load(arquivo)
    
soma = 0
maior = 0
linha_maior = None
i=0


for x in range(len(matriz)):
    i+=1
    soma = 0
    for y in range(len(matriz)):
        soma += matriz[x][y]
    if (soma > maior):
        maior = soma
        linha_maior = x
    continue

print(f"A linha com maior soma {linha_maior + 1} com a soma de: {maior}")