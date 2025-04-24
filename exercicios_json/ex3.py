# Contar quantos números ímpares existem na matriz

import json

with open("matriz.json", "r") as arquivo:
    matriz = json.load(arquivo)
    
count = 0    

for x in range(len(matriz)):
    for num in matriz[x]:
        if (num % 2 == 0):
            count+=1

print(f"Existem {count} números pares na matriz")