
# 🧩 Exercícios - Nível Iniciante

1. **Criar um tabuleiro simples (matriz 5x5)**
   - Objetivo: Preencher e exibir um tabuleiro com índices de 0 a 24.
   - Extras: Mostrar coordenadas como (linha, coluna).

2. **Posicionar um jogador no início**
   - Objetivo: Definir o jogador na posição (0,0) e exibir no tabuleiro como P.

3. **Movimentar o jogador com base em um número fixo**
   - Exemplo: o jogador anda 4 casas.
   - Atualizar a posição dele na matriz (linha x coluna).

4. **Detectar final do tabuleiro**
   - Se o jogador andar além da casa final, mostrar “Fim do jogo”.

5. **Mostrar número da casa no tabuleiro**
   - Preencher a matriz com número de casas (1, 2, 3… até 25).

---

# 🎯 Exercícios - Nível Intermediário

6. **Criar lista de comércios em posições aleatórias**
   - Exemplo: C representa comércio.
   - Gerar 5 comércios em posições aleatórias da matriz.

7. **Comprar comércio**
   - Se o jogador cair em um comércio (C), pode comprar se tiver saldo.
   - Atualizar matriz para mostrar dono (ex: J1).

8. **Criar mais de um jogador**
   - Jogador 1 e Jogador 2 se revezam nas jogadas.
   - Exibir turnos e posições no tabuleiro.

9. **Criar saldo para cada jogador**
   - Cada jogador começa com 1000.
   - Se comprar um comércio, gasta 300.
   - Mostrar saldo atual após cada turno.

10. **Cobrar aluguel**
    - Se o jogador cair num comércio do outro, pagar aluguel (100).

---

# 🧠 Exercícios - Nível Avançado

11. **Criar função de rolar dado (1 a 6)**
    - Rolar o dado antes de cada jogada para andar as casas.

12. **Criar tipos de casas**
    - Casas especiais como:
      - `!` → perde 200
      - `?` → sorte ou revés (+100 ou -100)
      - `*` → vai para próxima linha
    - Representar na matriz e definir lógica.

13. **Armazenar histórico de jogadas**
    - Exibir todas as jogadas feitas, saldo e casas visitadas.

14. **Criar sistema de falência**
    - Se o jogador ficar com saldo < 0, ele perde.

15. **Vencer por maior patrimônio**
    - Ao final de 15 rodadas, vence quem tiver mais saldo + propriedades.

---

# 🔄 Desafios Extras

- Adicionar um menu com opções: jogar, ver regras, sair.
- Exportar o histórico da partida para um `.txt`.
- Criar uma função que salva e carrega o jogo.
