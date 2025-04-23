import os

tamanho = 15
pos_jogador_index = 0

def gerar_perimetro(N):
    perimetro = []
    
    for i in range(N):
        perimetro.append((0, i))
        
    for i in range(1, N-1):
        perimetro.append((i, N-1))
        
    for i in range(N-1, -1, -1):
        perimetro.append((N-1, i))
        
    for i in range(N-2, 0, -1):
        perimetro.append((i, 0))
        
    return perimetro

def gerar_tabuleiro(N):
    tabuleiro = [[' ' for _ in range(N)] for _ in range(N)]
    perimetro = gerar_perimetro(N)
    
    for x, y in perimetro:
        tabuleiro[x][y] = '.'
    
    return tabuleiro

def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('  '.join(linha))
    print()

def calcular_andar(andar, pos_jogador_index, perimetro):
    for _ in range(andar):
        pos_jogador_index = (pos_jogador_index + 1) % len(perimetro)
    return pos_jogador_index
        
 
def atualizar_tabuleiro(tabuleiro, perimetro, pos_jogador_index):
    pos_jogador = perimetro[pos_jogador_index]
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            tabuleiro[i][j] = ' '
    
    for x, y in perimetro:
        tabuleiro[x][y] = '.'
        
    x, y = pos_jogador
    tabuleiro[x][y] = 'J'
    
    mostrar_tabuleiro(tabuleiro)
        
tabuleiro = gerar_tabuleiro(tamanho)
perimetro = gerar_perimetro(tamanho)

while True:
    atualizar_tabuleiro(tabuleiro, perimetro, pos_jogador_index)
    print(f"Posição jogador: {pos_jogador_index + 1}")
    andar_casas = input("\n\nQuantas casas deseja andar: ")
    
    try:
        andar = int(andar_casas)
    except:
        os.system("cls")
        print("Valor inserido não é número!")
        continue
    
    if (andar > 5 or andar < 1):
        os.system("cls")
        print("\nLimite para andar atigindo!" if andar > 5 else "\nLimite minimo atigindo!")
        print('Limite: 5\n\n')
        continue
    
    os.system("cls")
    pos_jogador_index = calcular_andar(andar, pos_jogador_index, perimetro)