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
 
# Criando dicionários para player e inimigos

player = {
    "vida": 100,
    "pos": [0,0]
}

inimigos = [{"vida": 50, "pos": [0,0]} for _ in range(3)]

# Aleatorizando localização dos inimigos

for inimigo in inimigos:
    cond = False
    
    if (inimigo["pos"] == (0,0)):
        while True:
            linha_aleatoria = random.randint(0, len(matriz) - 1)
            coluna_aleatoria = random.randint(0, len(matriz[0]) - 1)
            pos_aleatoria = (linha_aleatoria, coluna_aleatoria)
            
            if (pos_aleatoria == (0,0)):
                continue
            
            for outro_monstro in inimigos:
                if outro_monstro["pos"] == pos_aleatoria:
                    cond = True
                    break
            
            if cond:
                cond = False
                continue
            
            inimigo["pos"] = pos_aleatoria
            break

def mostrar_tabela(tabela):
    limpar_tela()
    for linha in tabela:
        print('  '.join(linha))
    print()
    

def limpar_tabela(tabela):
    for x in range(len(tabela)):
        for y in range (len(tabela)):
            tabela[x][y] = ''

def atualizar_tabela(tabela, jogador, monstros):
    xP, yP = jogador["pos"]
    # pos_monstros = [()]
    limpar_tabela(tabela)
    
    # for monstro in monstros:
    #     pos_monstros.append(monstro["pos"])
    
    for i in range(len(tabela)):
        for j in range(len(tabela)):
            tabela[i][j] = ' . '

    tabela[xP][yP] = ' P '
    mostrar_tabela(tabela)

def mover_jogador(direcao, jogador, tabela, monstros):
    if direcao[0]:
        if direcao[1]:
            pos_nova = jogador["pos"][0] + 1
            if pos_nova < len(tabela):
                jogador["pos"][0] = pos_nova
        else:
            pos_nova = jogador["pos"][0] - 1
            if 0 <= pos_nova:
                jogador["pos"][0] = pos_nova
    else:
        if direcao[1]:
            pos_nova = jogador["pos"][1] + 1
            if pos_nova < len(tabela[0]):
                jogador["pos"][1] = pos_nova
        else:
            pos_nova = jogador["pos"][1] - 1
            if 0 <= pos_nova:
                jogador["pos"][1] = pos_nova
    atualizar_tabela(tabela, jogador,  monstros)



while True:
    atualizar_tabela(matriz, player, inimigos)
    andar = input("\n\nDigite as teclas W, A, S, D para se movimentar pelo tabuleiro\n\n").upper()
    if andar not in ("W", "A", "S", "D"): continue
        
    if (andar == "W"):
        direcao = [True, False]
    elif (andar == "A"):
        direcao = [False, False]
    elif(andar == "S"):
        direcao = [True, True]
    elif(andar == "D"):
        direcao = [False, True]
    mover_jogador(direcao, player, matriz, inimigos)