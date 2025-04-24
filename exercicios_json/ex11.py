# 11. Sistema de Batalha com Matriz
# Descrição:

# Matriz 10x10.
# Jogador começa com 100 de vida.
# Monstros com 50 de vida em posições aleatórias.
# Ao encontrar um monstro, ocorre uma batalha (10 de dano por turno).
# O jogo termina com todos os monstros mortos ou o jogador derrotado.
# Controles:

# W (cima), A (esquerda), S (baixo), D (direita).
# Não pode sair da matriz.

import json
import random
import os

# Limpar a tela para reescrever a tabela

def limpar_tela():
    sistema = os.name
    if sistema == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Obtento matriz

with open("matriz_grande.json", "r") as arquivo:
    matriz = json.load(arquivo)
 
# Criando dicionários para jogador e monstros

jogador = {
    "vida": 100,
    "pos": (0,0)
}

monstros = [
    {"vida": 50, "pos": (0,0)},
    {"vida": 50, "pos": (0,0)},
    {"vida": 50, "pos": (0,0)}
]

# Aleatorizando localização dos monstros

for monstro in monstros:
    cond = False
    
    if (monstro["pos"] == (0,0)):
        while True:
            linha_aleatoria = random.randint(0, len(matriz) - 1)
            coluna_aleatoria = random.randint(0, len(matriz[0]) - 1)
            pos_aleatoria = (linha_aleatoria, coluna_aleatoria)
            
            if (pos_aleatoria == (0,0)):
                continue
            
            for outro_monstro in monstros:
                if outro_monstro["pos"] == pos_aleatoria:
                    cond = True
                    break
            
            if cond:
                cond = False
                continue
            
            monstro["pos"] = pos_aleatoria
            break

def mostrar_tabela(tabela):
    limpar_tela()
    for linha in tabela:
        print('  '.join(linha))
    print()

def limpar_tabela(tabela):
    for x in range(len(tabela)):
        for y in range (len(tabela)):
            tabela[x][y] = '   '

def atualizar_tabela(tabela, jogador, monstros):
    xP, yP = jogador["pos"]
    pos_monstros = [()]
    limpar_tabela(tabela)
    
    for monstro in monstros:
        pos_monstros.append(monstro["pos"])
    
    for i in range(len(tabela)):
        for j in range(len(tabela)):
            tabela[i][j] = '  .  '

    tabela[xP][yP] = '  P  '

def mover_jogador(direcao, jogador, tabela):
    if direcao[0]:
        if direcao[1]:
            pos_nova = jogador["pos"][0] + 1
            if pos_nova <= len(tabela):
                jogador["pos"][0] = pos_nova
        else:
            jogador["pos"][0]-=1
    else:
        if direcao[1]:
            ...
        else:
            ...