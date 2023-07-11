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

$\text{fator de balanceamento} = \text{altura subárvore esquerda} - \text{altura
subárvore direita}$

#### Operações
Se as operações de remoção ou inserção de um nó tornarem a árvores desbalanceada
é necessário o uso de rotações para garantir o fator de balanceamento.

- **Rotação a esquerda**:
    - Utilizada quando a sub árvore direta for maior que a esquerda, ou seja o nó
    pai tem o fator de balanceamento menor que -1.
    - Sendo y o filho direito de x, se y possuir uma sub árvore a esquerda (sub)
    então ela deve se tornar filho direito de x e y vai se tornar o pai de x.
```py
def left_rotate(x):
    y = x.right
    sub = y.left
    x.right = sub
    y.left = x
    return y
```
- **Rotação a direita**:
    - Utilizada quando a sub árvore esquerda for maior que a direita, ou seja o nó
    pai tem o fator de balanceamento maior que 1.
    - Sendo x o filho esquerdo de x, se x possuir uma sub árvore a direita (sub),
    então ela deve se tornar filha esquerda de y e x vai se tornar o pai de y.
```py
def right_rotate(y):
    x = y.left
    sub = x.right
    y.left = sub
    x.right = y
    return x
```
- **Rotação esquerda direita**:
    - Nesse caso, vamos supor que y é o filho direito de x que por sua vez é o
    filho esquerdo de z.
    - x e z apresentam fatos de balanceamento fora do intervalo, sendo $fb(x) < -1
    \space \text{e} \space fb(z) > 1$.
    - Dessa forma para regular o fator de balanceamento, z deve se tornar o filho
    direito de y e por outro lado x deve se tornar o filho esquerdo de y.
```py
def left_right_rotate(z):
    x = z.left
    y = left_rotate(x)
    w = right_rotate(y)
    return w
```
- **Rotação direita esquerda**:
    - Nesse caso, teremos que supor que y é o filho esquerdo de x, que por sua
    vez é filho direito de z.
    - x e z vão estar com o fator de balanceamento fora do intervalo, sendo 
    $fb(x)> 1 \space \text{e} \space fb(z) < -1$.
    - Dessa forma para deixar a árvore balanceada, z deve passar a ser o filho
    esquerdo de y e do outro lado x passa a ser filho direito de y.
```py
def right_left_rotate(z):
    x = z.right
    y = right_rotate(x)
    w = left_rotate(y)
    return w
```
#### Inserção
Uma inserção pode gerar um desbalanceamento em toda a árvore, deve-se proceder
operações de rotação no nó desbalanceado mais próximo.
- Se fator de balanço desse nó for maior que 1:
    - Se novo nó for menor ou igual que filho esquerdo do nó desbalanceado deve-se
    fazer a **rotação a direita**
    - Se o novo nó for maior que o filho esquerdo do nó desbalanceado deve-se fazer
    a **rotação esquerda direita**
- Agora se o balanceamento desse nó for menor que -1:
    - Se o novo nó for maior que o filho direito do nó desbalanceado então ocorre
    a rotação a esquerda
    - Por outro lado se o novo no for menor ou igual ao filho direito do nó 
    desbalanceado então faz a **rotação direita esquerda**

#### Remoção 
A remoção apresenta 3 casos básicos:
- Nó removido é uma folha.
    - Devemos checar o fator de balanceamento dos antecessores.

- Nó removido é possui 1 filho.
    - Devemos substituir o nó pelo seu filho e checar o fator de balanceamento
    dos antecessores.

- Nó removido possui 2 filhos.
    - Devemos achar o sucessor para substituir pelo nó removido em seguida checar
    o fator de balanceamento dos antecessores
Caso o antecessores estejam fora do intervalo:
```py
def balancear(x):
    if fator_balanceamento(x) > 1:
        if fator_balanceamento(x.left) >= 0:
            right_rotate(x)
        else:
            left_right_rotate(x)
        return 
    if fator_balanceamento(x) <= -1:
        if fator_balanceamento(x.left) <= 0:
            left_rotate(x)
        else:
            right_left_rotate(x)
        return 
    return 
```
