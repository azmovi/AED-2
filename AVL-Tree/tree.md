# AVL Tree
    Antônio Cícero Amorim de Azevedo - RA: 811455
- Algoritmo criado pelo Adelson-Velsky e Landis.
- Se baseia em uma árvore de busca binária com auto balanceamento.

### Estrutura de dados iniciais:
#### Árvore:
- Conjunto de entidades chamadas de nó.
- Conectados por uma arestas. 
- Cada nó contem um dado
- **Raiz**: nó mais alto da árvore.
- **Folha**: nó sem filho.
- **Altura**: geração de um nó na árvore.
#### Árvore Binária de Busca:
- O pai deve apresentar no máximo 2 filhos.
- O filho da esquerda um valor menor que o seu pai.
- O filho da direita tem um valor maior que seu pai

### Árvore Binária de Busca Balanceada - AVL
- A diferença entre uma árvore de busca normal e uma balanceada é existência de
fator de balanceamento que pode atingir apenas 3 valores (-1, 0, 1).

$\text{fator de balanceamento} = \text{altura subárvore esquerda} - \text{altura subárvore direita}$

