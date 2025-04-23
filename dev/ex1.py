N = 5
tabuleiro = [[' ' for _ in range(N)] for _ in range(N)]

perimetro = []

for i in range(N):
    perimetro.append((0, i))

for i in range(1, N-1):
    perimetro.append((i, N-1))

for i in range(N-1, -1, -1):
    perimetro.append((N-1, i))

for i in range(N-2, 0, -1):
    perimetro.append((i, 0))

for x, y in perimetro:
    if ((x == 0 or x == N-1) and (y == 0 or y == N-1)):
        tabuleiro[x][y] = 'O'
    elif (x == 0 or x == N-1):
        tabuleiro[x][y] = 'X'
    else:
        tabuleiro[x][y] = 'Y'
        
    
for linha in tabuleiro:
    print('  '.join(linha))