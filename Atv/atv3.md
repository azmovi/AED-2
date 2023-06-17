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
def heapfy(vector, n, indice = 0):
    maior = indice
    left = 2*indice + 1
    right = 2*indice + 2

    if left < n and vector[left] > vector[maior]:
        maior = left 
    if right < n and vector[right] > vector[maior]:
        maior = right

    if maior != indice:
        vector[indice], vector[maior] = vector[maior], vector[indice]
        heapfy(vector, n,  maior)
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
        heapify(vector, len(vector), i)
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
        heapify(vector, i)
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
$\newline$
```vetor = [17, 12, 15, 9, 8, 6, 7, 4, 3, -1]```
$\newline$
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
Remove(17)
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
```vetor = [15, 12, 7, 9, 8, 6, -1, 4, 3, 17]```
$\newline$
Heapfy(-1)
```
                                                15
                                               / \
                                              /   \
                                             12    7
                                            / \   / \
                                           9   8 6  -1
                                          / \  
                                         4   3  
```
```vetor = [3, 12, 7, 9, 8, 6, -1, 4, 15, 17]```
$\newline$
Troca(15, 3)
```
                                                3
                                               / \
                                              /   \
                                             12    7
                                            / \   / \
                                           9   8 6  -1
                                          / \  
                                         4   15  
```
```vetor = [3, 12, 7, 9, 8, 6, -1, 4, 15, 17]```
$\newline$
Remove(15)
```
                                                3
                                               / \
                                              /   \
                                             12    7
                                            / \   / \
                                           9   8 6  -1
                                          /
                                         4
```
```vetor = [12, 9, 7, 4, 8, 6, -1, 3, 15, 17]```
$\newline$
Heapfy(3)
```
                                                12
                                               / \
                                              /   \
                                             9     7
                                            / \   / \
                                           4   8 6  -1
                                          /
                                         3
```
```vetor = [3, 9, 7, 4, 8, 6, -1, 12, 15, 17]```
$\newline$
Troca(12, 3)
```
                                                3
                                               / \
                                              /   \
                                             9     7
                                            / \   / \
                                           4   8 6  -1
                                          /
                                         12
```
```vetor = [3, 9, 7, 4, 8, 6, -1, 12, 15, 17]```
$\newline$
Remove(12)
```
                                                3
                                               / \
                                              /   \
                                             9     7
                                            / \   / \
                                           4   8 6  -1
```
```vetor = [9, 8, 7, 4, 3, 6, -1, 12, 15, 17]```
$\newline$
Heapfy(3)
```
                                                9
                                               / \
                                              /   \
                                             8     7
                                            / \   / \
                                           4   3 6  -1
```
```vetor = [-1, 8, 7, 4, 3, 6, 9, 12, 15, 17]```
$\newline$
Troca(9, -1)
```
                                               -1
                                               / \
                                              /   \
                                             8     7
                                            / \   / \
                                           4  3  6   9
```
```vetor = [-1, 8, 7, 4, 3, 6, 9, 12, 15, 17]```
$\newline$
Remove(9)
```
                                               -1
                                               / \
                                              /   \
                                             8     7
                                            / \   /
                                           4  3  6
```
```vetor = [8, 4, 7, -1, 3, 6, 9, 12, 15, 17]```
$\newline$
Heapfy(-1)
```
                                                8
                                               / \
                                              /   \
                                             4     7
                                            / \   /
                                          -1   3 6
```
```vetor = [6, 4, 7, -1, 3, 8, 9, 12, 15, 17]```
$\newline$
Troca(8, 6)
```
                                                6
                                               / \
                                              /   \
                                             4     7
                                            / \   /
                                          -1   3 8
```
```vetor = [6, 4, 7, -1, 3, 8, 9, 12, 15, 17]```
$\newline$
Remove(8)
```
                                                6
                                               / \
                                              /   \
                                             4     7
                                            / \
                                          -1   3
```
```vetor = [7, 4, 6, -1, 3, 8, 9, 12, 15, 17]```
$\newline$
Heapfy(6)
```
                                                7
                                               / \
                                              /   \
                                             4     6
                                            / \
                                          -1   3
```
```vetor = [7, 4, 6, -1, 3, 8, 9, 12, 15, 17]```
$\newline$
Troca(7, 3)
```
                                                7
                                               / \
                                              /   \
                                             4     6
                                            / \
                                          -1   3
```
```vetor = [3, 4, 6, -1, 7, 8, 9, 12, 15, 17]```
$\newline$
Troca(7, 3)
```
                                                3
                                               / \
                                              /   \
                                             4     6
                                            / \
                                          -1   7
```
```vetor = [3, 4, 6, -1, 7, 8, 9, 12, 15, 17]```
$\newline$
Remove(7)
```
                                                3
                                               / \
                                              /   \
                                             4     6
                                            /
                                          -1
```
```vetor = [6, 4, 3, -1, 7, 8, 9, 12, 15, 17]```
$\newline$
Heapfy(3)
```
                                                6
                                               / \
                                              /   \
                                             4     3
                                            /
                                          -1
```
```vetor = [-1, 4, 3, 6, 7, 8, 9, 12, 15, 17]```
$\newline$
Troca(6, -1)
```
                                               -1
                                               / \
                                              /   \
                                             4     3
                                            /
                                           6
```
```vetor = [-1, 4, 3, 6, 7, 8, 9, 12, 15, 17]```
$\newline$
Remove(6)
```
                                               -1
                                               / \
                                              /   \
                                             4     3
```
```vetor = [4, -1, 3, 6, 7, 8, 9, 12, 15, 17]```
$\newline$
Heapfy(-1)
```
                                                4
                                               / \
                                              /   \
                                             -1    3
```
```vetor = [3, -1, 4, 6, 7, 8, 9, 12, 15, 17]```
$\newline$
Remove(4)
```
                                                3
                                               /
                                              /
                                             -1    
```
```vetor = [3, -1, 4, 6, 7, 8, 9, 12, 15, 17]```
$\newline$
Remove(4)
```
                                                3
                                               /
                                              /
                                             -1    
```
```vetor = [3, -1, 4, 6, 7, 8, 9, 12, 15, 17]```
$\newline$
Heapfy(3)
```
                                                3
                                               /
                                              /
                                             -1    
```
```vetor = [-1, 3, 4, 6, 7, 8, 9, 12, 15, 17]```
$\newline$
Troca(3, -1)
```
                                               -1
                                               /
                                              /
                                             3    
```
```vetor = [-1, 3, 4, 6, 7, 8, 9, 12, 15, 17]```
$\newline$
Remove(3)
```
                                               -1
```
- Um elemento na heap, dessa forma ela se encontra ordenada, dessa forma nosso
vetor de elementos é:

```vetor = [-1, 3, 4, 6, 7, 8, 9, 12, 15, 17]```


### 2 - Questão 
- Qual é a complexidade do _**Heap Sort**_ no pior caso: