# Trabalho 4 - Levada 
    Nome: Antônio Cícero Amorim de Azevedo
    Ra: 811455 
> Árvore Binária de Busca
### 1 - Questão 
- Dado uma árvore binária fornecer as formas de se percorrer ela.
```
                                                 A
                                                / \
                                               /   \
                                              /     \
                                             /       \
                                            /         \
                                           B           C
                                          / \         / \
                                         /   \       /   \
                                        D     E     F     G
                                             / \   / \ 
                                            H   I J   K 
```
###### A) Preorder:
```py
def preoder(node):
    if node != None:
        print(node.data)
        preorder(node.left)
        preorder(node.right)
    return
```
- **Output** = [A, B, D, E, H, I, C, F, J, K, G]


###### B) Inorder:
```py
def inorder(node):
    if node != None:
        preorder(node.left)
        print(node.data)
        preorder(node.right)
    return
```
- **Output** = [D, B, H, E, I, A, J, F, K, C, G]

###### C) Postorder:
```py
def postoder(node):
    if node != None:
        preorder(node.left)
        preorder(node.right)
        print(node.data)
    return
```
- **Output** = [D, H, I, E, B, J, K, F, G, C, A]

### 2 - Questão 
- Provar que que a busca em um árvore binária pode variar de logarítmica a linear
```py
def search_tree(no, valor):
    if no == None or no.key == key:
        return x
    if no.key > k:
        return search_tree(no.left, k)
    else:
        return search_tree(no.right, k)
```
Dado um árvore com N nós, teremos:
- L nós na subárvore a esquerda
- N - L - 1 nós na subárvore a direita
Dessa forma teremos por recorrência a seguinte equação:
$$ T(N) = T(L) + T(N-L-1) + C $$
- Sendo $C$ uma constante, que pode representar uma atribuição, uma chamada de
função como print(), len() entre outras coisas que não dependem do tamanho da
árvore e executam com tempo de complexidade O(1).
###### Melhor caso: árvore binária perfeita.

$$ T(N) = T(\frac{N}{2}) + T(\frac{N}{2}) + C $$
$$ T(N) = 2T(\frac{N}{2}) + C $$
- Onde os dois lados apresentam o número igual de subárvores
$$ T(N) = 2(2T(\frac{n}{4}) + C) + C $$
$$ T(N) = 4T(\frac{n}{4}) + 2C + C $$
$$ T(N) = 4T(\frac{n}{4}) + 3C $$
- Generalizado:
$$ T(N) = \sum_{i=1}^{k} 2^iT(\frac{n}{2^i}) + C*i $$

- Onde o critério de parada será:
$$ \frac{n}{2^k} = 1 $$
$$ n = 2^k $$
$$ \log_{2}n = k * \log_{2}2$$
$$ \log_{2}n = k $$

- Colocando na equação principal:
$$ T(N) = \sum_{i=1}^{\log_{2}n} 2^iT(\frac{n}{2^i}) + \sum_{i=1}^{\log_{2}2} C*i $$

- Expandido os somatórios: 
$$ T(N) = \sum_{i=1}^{\log_{2}n} 2^iT(\frac{n}{2^i}) + \sum_{i=1}^{\log_{2}2} C*i $$
$$ T(N) =  2^1 * 2^2 *... *2^k + C*(1 + 2 ... +k) $$
$$ T(N) =  2^{1 + 2 + ... +k} + C*(1 + 2 ... +k) $$
$$ T(N) =  2^{\frac{(1 + k)*1}{2}} + C*(\frac{(1 + k)*1}{2}) $$

- Substituindo o K, que represeta a altura da árvore binária.
$$ T(N) =  2^{\frac{(1 + \log_{2}n)}{2}} + C*(\frac{(1 + \log_{2}n)}{2}) $$

- Removendo as constantes:
$$ T(N) =  2^{\log_{2}n} + \log_{2}n $$
$$ T(N) =  \log_{2}n + \log_{2}n $$
$$ T(N) =  2\log_{2}n $$

Concluimos que para o melhor caso a complexidade de busca será na ordem de:
$$ O(\log_{2}n) $$

###### Pior caso: Todo nó apresenta apenas 1 filho.
$$ T(N) = T(N-1) + T(0) + C $$
$$ T(N-1) = T(N-1-1) + T(0) + C + T(0) + C $$

- Dessa forma a árvore irá se comportar como um vetor normal de busca sequencial.
$$T(N) = \sum_{i=1}^{n} T(n-i) + C $$
$$T(N) = \sum_{i=1}^{n} T(n-i) + \sum_{i=1}^{n} C $$

- Expandido os somatórios:
$$T(N) = n * 1 + n*C $$
$$T(N) = n (1 + C) $$

- Removendo as constantes ficamos com a complexidade de busca igual a:
$$ O(n) $$

**Dessa forma conseguimos perceber que a complexidade de tempo para se encontrar
um item em uma árvore binária de busca pode variar entre:**
$$O(\log_{2}n)\text{ ate }O(n)$$


### 3 - Questão
- Explicar o algoritmo de inserção em uma árvore binária
```py
def insert_tree(tree, novo_no):
    x = tree.root
    y = None
    while x != None:
        y = x
        if novo_no.key < x.key:
            x = x.left
        else:
            x = x.right

    novo_no.pai = y
    if y == None:
        tree.root = novo_no
    else:
        if y.key > novo_no.key:
            y.left = novo_no
        else:
            y.right = novo_no
    return 
```
- Recebemos como parâmetros a instancia/objeto que representa uma árvore binária
que queremos analisar e uma outra instancia/objeto que representa um nó na qual
iremos inserir nesse árvore binária.

- Após isso passamos para um loop do tipo _while_ para encontrar a posição que
o nosso nó novo deve estar localizado na árvore binária seguindo a regra que o
filho direito deve ser obrigatoriamente **maior** que o seu pai, e o filho esquerdo
deve ser obrigatoriamente **menor** que seu pai.

- Quando sair do loop, devemos verificar se a árvore era vazia ou não. Dessa forma,
se ela for vazia o novo valor sera a própria raiz da árvore binária.

- Caso não seja vazia verificamos em que ramo o novo valor se encontra, se ele for
maior que seu pai irá para a direita se não ele irá para a esquerda, finalizando 
o algoritmo de inserção.

### 4 - Questão
- Explicar o algoritmo de remoção de um nó em uma árvore binária.
```py
def remove_no(tree, no):
    if no.left == None:
        transplant(tree, no, no.right)
    elif no.right == None:
        transplant(tree, no, no.left)
    else:
        sucessor = tree_minimum(no.right)
        if sucessor != no.right:
            transplant(tree, sucessor, sucessor.right)
            sucessor.right = no.right
            no.right = None
            sucessor.right.pai = sucessor
        transplant(tree, no, sucessor)
        sucessor.left = no.left
        no.left = None
        sucessor.left.pai = sucessor
    return

def transplant(tree, atual, novo):
    if atual.pai == None:
        tree.root = novo
    elif atual == atual.pai.left:
        atual.pai.left = novo
    else:
        atual.pai.right = novo
    if novo != None:
        novo.pai = atual.pai
        atual.pai = None
    return 

def tree_minimum(no):
    while no.left != None:
        no = no.left
    return no

```
Teremos 3 casos possíveis na remoção de um nó
- Se o nó **não** tiver um filho:
    - Basta remover a folha normalmente.
- Se o nó tem **um** filho:
    - o filho do nó removido deve-se se juntar ao pai do nó removido.
- Se o nó tem **dois** filhos:
    - Devemos encontrar o sucessor da direita do nó removido na sua sub árvore.
    A remoção do sucessor na sua posição atual entra em um desses 3 casos vistos.

Funcionamento da função _transplant_
- Ela é responsável por trocar as referencias de dois nos, onde o nó atual perde
sua posição para um novo nó.

### 5 - Questão 
- Duas algoritmos sobre árvore binária de busca.
###### a) Algoritmo para encontrar o menor elemento:
```py
def min_tree(tree):
    no = tree.root
    while no.left != None:
        no = no.left
    return no.data
```
###### b) Algoritmo para encontrar a altura de um nó:
```py
def altura(no):
    if no == None:
        return 1
    else:
        esquerda = altura(no.left)
        direita = altura(no.right)
        return max(esquerda, direita)
    return
```
