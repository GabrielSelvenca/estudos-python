## 🟢 **Nível Básico**

**1.** Somar todos os elementos de um array  
**2.** Somar os elementos da diagonal principal de uma matriz  
**3.** Contar quantos números ímpares existem na matriz  
**4.** Verificar se um número existe na matriz e retornar sua posição  
**5.** Trocar a diagonal principal pela diagonal secundária  

---

## 🟡 **Nível Intermediário**

**6.** Girar a matriz em 90 graus (sentido horário)  
**7.** Identificar a linha com maior soma  
**8.** Transformar uma matriz NxN em uma lista com todos os valores ordenados  
**9.** Trocar os maiores valores da matriz por -1  
**10.** Criar uma nova matriz onde cada célula seja a média dos seus vizinhos  

---

## 🔴 **Nível Avançado**

**11.** Sistema de Batalha com Matriz  
**Descrição:**  
- Matriz 10x10.  
- Jogador começa com 100 de vida.  
- Monstros com 50 de vida em posições aleatórias.  
- Ao encontrar um monstro, ocorre uma batalha (10 de dano por turno).  
- O jogo termina com todos os monstros mortos ou o jogador derrotado.  

**Controles:**  
- W (cima), A (esquerda), S (baixo), D (direita).  
- Não pode sair da matriz.

---

**12.** Jogo da Vida (simplificado)  
**Descrição:**  
- Matriz NxN com células vivas (1) ou mortas (0).  
- A cada rodada, as células mudam com base nas vizinhas.

**Regras:**  
- Viva com 2 ou 3 vizinhas vivas → continua viva.  
- Morta com 3 vizinhas vivas → revive.  
- Caso contrário, morre ou continua morta.

**Objetivo:**  
- Rodar por 10 ciclos e exibir cada estado da matriz.

---

**13.** Simulação de Calor em uma Placa  
**Descrição:**  
- Matriz NxN com valores representando temperatura.  
- Borda da matriz é fixa.  
- As células internas são atualizadas com a média dos 4 vizinhos diretos (cima, baixo, esquerda, direita).  

**Objetivo:**  
- Rodar por 10 ciclos e mostrar a distribuição do calor.

---

**14.** Pathfinding Simples em Matriz com Obstáculos  
**Descrição:**  
- Matriz NxN com:
  - `0` = caminho livre  
  - `1` = obstáculo  
  - `A` = início  
  - `B` = destino  

**Objetivo:**  
- Usar busca em largura (BFS) para encontrar um caminho de A até B evitando obstáculos.  
- Mostrar o caminho marcado com `*`.