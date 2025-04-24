# Verificar se um número existe na matriz e retornar sua posição

import json

with open("matriz.json", "r") as arquivo:
    matriz = json.load(arquivo)

while True:    
    busca = input("Digite um número para buscar: ")
    try:
        busca_num = int(busca)
    except:
        print("\nDigite um número válido!\n\n")
        continue
    
    num_achado = None
    
    for index_X in range(len(matriz)):
        for index_Y in range(len(matriz[index_X])):
            if matriz[index_X][index_Y] == busca_num:
                num_achado = matriz[index_X][index_Y]
                pos_num = (index_X, index_Y)
                break
    
    if (num_achado != None):
        print(f"\n\nNúmero {num_achado} encontrado na posição {pos_num} da matriz")
        break
    else:
        print(f"O número {busca_num} não existe na matriz atual\n\n")
        continue