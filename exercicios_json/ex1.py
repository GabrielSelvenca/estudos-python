# Somar todos os elementos de um array

import json

with open("array.json", "r") as arquivo:
    array = json.load(arquivo)
    
soma = 0

for num in array:
    soma+=num

print(f"Soma total da array: {soma}")