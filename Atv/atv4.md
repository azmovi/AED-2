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

Dado um árvore com N nós, teremos:
- L nós na subárvore a esquerda
- N - L - 1 nós na subárvore a direita
Dessa forma teremos por recorrência a seguinte equação:
$$ T(N) = T(L) + T(N-L-1) + C $$
- Sendo $C$ uma constante, que pode representar uma atribuição, uma chamada de
função como print(), len() entre outras coisas que não dependem do tamanho da
árvore e executam com tempo de complexidade O(1).
###### Melhor caso: árvore binária pefeita.

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






