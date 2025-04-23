import os
N = 5

def gerar_perimetro(N):
    p = []
    for i in range(N):
        p.append((0, i))

    for i in range(1, N-1):
        p.append((i, N-1))

    for i in range(N-1, -1, -1):
        p.append((N-1, i))

    for i in range(N-2, 0, -1):
        p.append((i, 0))
        
    return p

def gerar_tabuleiro(N, p):
    t = [[' ' for _ in range(N)] for _ in range(N)]
    
    for x, y in p:
        t[x][y] = '.'
        
    return t

def mostrar_tabuleiro(tabuleiro):
    os.system("cls")
    for linha in tabuleiro:
        print('  '.join(linha))

def atualizar_tabuleiro(t, p, pji):
    pos_jogador = p[pji]
    
    for i in range(len(t)):
        for j in range(len(t[i])):
            t[i][j] = ' '
            
    for x, y in p:
        t[x][y] = '.'
        
    x, y = pos_jogador
    t[x][y] = 'P'

    mostrar_tabuleiro(t)
    
def calcular_movimentacao(posisao_jogador_index, p):
    for _ in range(2):
        posisao_jogador_index = (posisao_jogador_index + 1) % len(p)
    
    return posisao_jogador_index

posisao_jogador_index = 0

perimetro = gerar_perimetro(N)
tabuleiro = gerar_tabuleiro(N, perimetro)

atualizar_tabuleiro(tabuleiro, perimetro, posisao_jogador_index)

while True:
    andar = input("Aperte enter para andar 2 casas")
    posisao_jogador_index = calcular_movimentacao(posisao_jogador_index, perimetro)
    if (posisao_jogador_index == 0):
        os.system("cls")
        print("Fim do jogo.")
        break
    atualizar_tabuleiro(tabuleiro, perimetro, posisao_jogador_index)