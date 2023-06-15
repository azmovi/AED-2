# Trabalho 3 - Levada 
    Nome: Antônio Cícero Amorim de Azevedo
    Ra: 811455 

### 1 - Questão 
- Mostrar o passo a passo do _**Heap Sort**_ na seguinte lista:
    - [7, 4, 15, 9, -1, 6, 17, 12, 3, 8]

##### _Heap_ Conceito:
- Uma árvore binária **completa**:
    - Todos os níveis estão preenchidos, exceto o último que deve ter filhos a
    mais esquerda possível.
- Max _Heap_:
    - O nó pai é **maior** que o nó filho.
- Min _Heap_:
    - O nó pai é **menor** que o nó filho.

##### Árvore binária -> Heap (heapify):
- Processo de transformar uma árvore binária em uma _heap_ (máxima ou minima)
- Algorítimo para criar um _heap_ de máximo:
```py
def heapfy(vector, indice = 0):
    maior = indice
    left = 2*indice + 1
    right = 2*indice + 2

    if left < len(vector) and vector[left] > vector[maior]:
        maior = left 
    if right < len(vector) and vector[right] > vector[maior]:
        maior = right

    if maior != indice:
        vector[indice], vector[maior] = vector[maior], vector[indice]
        heapfy(vector, maior)
    return
```
###### Análise da Complexidade do _Heapfy_:
- Nessa análise vou declarar o nó da direta sendo o maior dado do vetor:
- A quantidade de interações sera igual a altura da árvore.
$$ T(n) = 1 + 1 + 1 + 1 + 1 + 2 + T(n-2^1) $$
$$ T(n) = 7 + T(n-2^1) $$
$$ T(n) = \sum_{i=1}^{h}T(n-2^i)$$
- Sendo h igual a altura da árvore podemos chegar na seguinte equação:
$$ n - 2^h = 0 $$
$$ n  = 2^h $$
$$ \log_{2}n = h $$
 - Dessa forma:
$$ T(n) = \sum_{i=1}^{h}7 + T(n-2^h) $$
$$ T(n) = 7 * h + 0 $$
$$ T(n) = 7 * \log_{2}n $$
- Concluindo que a complexidade da função heapfy é na ordem de:
$$ O(h) = O(\log_{2}n) $$

###### Construção da Heap (_build_heap_):
- Essa função é responsável por construir a heap utilizando o heapify, podendo
ser de máximo ou minimo. 
```py
def build_heap(vector):
    for i in range(len(vector)//2 - 1, -1, -1):
        heapify(vector, i)
    return
```
- O loop comecaçará pelo o possível pai mais a esquerda da árvore binária,
chamando a funçao do heapify.
###### Complexidade do do _Build Heap_:
$$ T(n) = \sum_{i = 0}^{\frac{n}{2} - 1} \log_{2}n $$
$$ T(n) = (\frac{n}{2} - 1) * \log_{2}n $$
$$ T(n) = \frac{n*\log_{2}n }{2} - \log_{2}n  $$
- Removendo as constantes:
$$ T(n) = n*\log_{2}n  - \log_{2}n  $$
- Dessa forma chegamas que a complexidade da funçao _build heap_:
$$ O(n*log_{2}n) $$

###### Desenvolvendo a lógica o _Heap Sort_
- Apenas a ultima folha pode ser retirada da heap.
- A raiz (maior elemento do vetor) troca de lugar com a ultima folha.
- Após a troca, a nova raiz deve achar seu local na heap, e a nova raiz será o 
novo maior valor presente na heap.

```py
def heap_sort(vector):
    heap_build(vector)
    for i in range(n-1, -1, -1):
        vector[i], vector[0] = vector[0], vector[i]
        heapify(vector[i:])
    return
```
###### Mostrando o passo a passo do **_Heap Sort_**
Vetor em um formato de árvore binária
```
                                                7
                                               / \
                                              /   \
                                             4     15
                                            / \   /  \
                                           9   -1 6   17
                                          / \   /
                                         12  3 8 
```
Troca(-1, 8)
```
                                                7
                                               / \
                                              /   \
                                             4     15
                                            / \   /  \
                                           9   8 6   17
                                          / \  /
                                         12  3-1 
```
Troca(9, 12)
```
                                                7
                                               / \
                                              /   \
                                             4     15
                                            / \   /  \
                                           12  8 6   17
                                          / \  /
                                         9   3-1 
```
Troca(15, 17)
```
                                                7
                                               / \
                                              /   \
                                             4     17
                                            / \   /  \
                                           12  8 6   15
                                          / \  /
                                         9   3-1 
```
Troca(4, 12)
```
                                                7
                                               / \
                                              /   \
                                             12    17
                                            / \   /  \
                                           4   8 6   15
                                          / \  /
                                         9   3-1 
```
Troca(4, 9)
```
                                                7
                                               / \
                                              /   \
                                             12    17
                                            / \   / \
                                           9   8 6   15
                                          / \  /
                                         4   3-1 
```
Troca(7, 17)
```
                                                17
                                               / \
                                              /   \
                                             12    7
                                            / \   / \
                                           9   8 6   15
                                          / \  /
                                         4   3-1 
```

Troca(7, 15)
```
                                                17
                                               / \
                                              /   \
                                             12    15
                                            / \   / \
                                           9   8 6   7
                                          / \  /
                                         4   3-1 
```
Agora o vetor está na ordem de uma heap de maximo.
```vetor = [17, 12, 15, 9, 8, 6, 7, 4, 3, -1]```
Próximo passo é fazer o processo de Heap Sort:

Troca(17, -1)
```
                                               -1
                                               / \
                                              /   \
                                             12    15
                                            / \   / \
                                           9   8 6   7
                                          / \  /
                                         4   3 17 
```
```vetor = [-1, 12, 15, 9, 8, 6, 7, 4, 3, 17]```
$\newline$
Remover o 17 da heap
```
                                               -1
                                               / \
                                              /   \
                                             12    15
                                            / \   / \
                                           9   8 6   7
                                          / \  
                                         4   3  
```
```vetor = [15, 12, 6, 9, 8, -1, 7, 4, 3, 17]```
$\newline$
Heapificar o valor -1
```
                                                15
                                               / \
                                              /   \
                                             12    6
                                            / \   / \
                                           9   8 -1   7
                                          / \  
                                         4   3  
```
