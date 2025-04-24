import json

matriz = []
contador = 1
for i in range(5):
    linha = []
    for j in range(5):
        linha.append(contador)
        contador += 1
    matriz.append(linha)

with open("matriz.json", "w") as arquivo:
    json.dump(matriz, arquivo)
    
matriz_grande = []
contador = 1
for i in range(10):
    linha = []
    for j in range(10):
        linha.append(contador)
        contador += 1
    matriz_grande.append(linha)
    
with open("matriz_grande.json", "w") as arquivo:
    json.dump(matriz_grande, arquivo)