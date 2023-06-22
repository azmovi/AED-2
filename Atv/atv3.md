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
$$ T(n) = \sum_{i = 0}^{\frac{n}{2} - 1} heapify(\frac{n}{2}-1-i) $$
$$ T(n) = \sum_{i = 0}^{\frac{n}{2} - 1} \log_{2}(\frac{n}{2}-1-i) $$
$$ T(n) = \log_{2}\frac{n}{2} - 1 + \log_{2}\frac{n}{2} - 2 + ...+\log_{2}
\frac{n}{2}- \frac{n}{2} $$
- Usando a propriedades do logaritmo.
$$ T(n) = \log_{2}((\frac{n}{2} - 1) *(\frac{n}{2} - 2) * ...* (\frac{n}{2}- \frac{n}{2}))$$
$$ T(n) = \log_{2}\frac{n}{2}!$$
- Usando a aproximação de Stirling:
$$ \frac{n}{2}! \approx \frac{n}{2} * \log_{2}\frac{n}{2} - \frac{n}{2} + O(\log_{2} \frac{n}{2} )$$

- Removendo as constantes.
$$ T(n) = n * \log_{2}n - n + O(\log_{2}n ) $$
- Dessa forma chegamos que o bigO do _Build Heap_ é

$$ O(n \log_{2}n)$$


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
- Algortimo complexo a baixo:
```py
def heapfy(vector, n, indice = 0):
    """  """
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

def build_heap(vector):
    """  """
    for i in range(len(vector)//2 - 1, -1, -1):
        heapify(vector, len(vector), i)
    return

def heap_sort(vector):
    """  """
    heap_build(vector)
    for i in range(n-1, -1, -1):
        vector[i], vector[0] = vector[0], vector[i]
        heapify(vector, i)
    return

```
- O algoritmo transforma todo vetor em uma _Heap_.
- Independente do caso, ele terá a mesma complexidade.
$$ T(n) = T(\text{BuildHeap}) + \sum_{i=1}^{n-1}(2+T(\text{heapify}(n-i))) $$
$$ T(n) = n*\log_{2}n  - \log_{2}n + \sum_{i=1}^{n-1}2+\sum_{i=1}^{n-1}T(\text{heapify}(n-i)) $$
$$ T(n) = n*\log_{2}n  - \log_{2}n + 2n + \sum_{i=1}^{n-1}T(\text{heapify}(n-i)) $$
$$ T(n) = n*\log_{2}n  - \log_{2}n + 2n + \sum_{i=1}^{n-1}\log_{2}(n-i) $$
- Desenvolvendo o somatório:
$$ \sum_{i=1}^{n-1}\log_{2}(n-i) = \log_{2}(n-1) + \log_{2}(n-2) +... + \log_{2}(n-(n-1)) $$
$$ \sum_{i=1}^{n}\log_{2}(n-i) = \log_{2}(n-1) * (n-2) * ...* \log_{2}(1) $$
$$ \sum_{i=1}^{n}\log_{2}(n-i) = \log_{2} n! $$

- Usando novamente a aproximação de Stiring:

$$ \log_{2}n! \approx n * \log_{2}n - n + O(\log_{2}n)$$

- Colocando da equação principal:

$$ T(n) = n*\log_{2}n  - \log_{2}n + 2n + \log_{2}n! $$
$$ T(n) = n*\log_{2}n  - \log_{2}n + 2n + n * \log_{2}n - n + O(\log_{2}n)$$
$$ T(n) = 2n*\log_{2}n  - \log_{2}n + n + O(\log_{2}n)$$
- Com essa equação podemos perceber que a complexidade do _**Heap Sort**_ é:
$$ O(n\log_{2}n) $$



### 3 - Questão 
- Provar que nenhum algoritmo de ordenação baseado em comparações (trocas) pode ter
complexidade menor que _O_($n\log_{2}n$)
- Podemos abstrair que todo algoritmo de ordenação pode ser representado por uma
árvore binária. 
- Outro fator será que as folhas dessa árvore serão todas as permutações possíveis
de um determinador vetor, ou seja _n!_
- Para o pior caso o algoritmo terá que fazer h comparações, sendo h a altura da
árvore binária.
- Dessa forma se uma árvore estiver perfeita o número máximo de filhos será igual
a $2^k$ 
- Com isso chegar a uma possível conclusão:
$$ 2^k \geq n! $$
- Desenvolvendo a expressão:
$$ \log_{2}2^k \geq \log_{2}n! $$
$$ k \geq \log_{2}n! $$
$$ k \geq \log_{2}(n * (n-1) * (n-2)*... * 1) $$
$$ k \geq \log_{2}(n) + \log_{2}(n-1) + \log_{2}(n-2)+... + \log_{2}(1) $$
$$ k \geq \sum_{i=1}^{n} \log_{2}i $$
$$ k \geq \int_{1}^{n} \log_{2}x * dx$$
- Desenvolvendo a integral:
$$ \int \log_{2}x * dx = x*\log_{2}x - \frac{x}{\ln2} $$

$$ \int_{1}^{n} \log_{2}x * dx = (n*\log_{2}n - \frac{n}{\ln2} ) - (1*\log_{2}1 - \frac{1}{\ln2} )$$
$$ \int_{1}^{n} \log_{2}x * dx = n*\log_{2}n - \frac{n}{\ln2}  + \frac{1}{\ln2} )$$
- Voltando para a equação inicial:

$$ k \geq n*\log_{2}n - \frac{n}{\ln2}  + \frac{1}{\ln2}  $$

- Dessa forma chegamos que o limite inferior de um algoritmo de ordenação baseado
em comparações é:
$$ \varOmega (n*\log_{2}n) $$

### 4 - Questão 
##### a) Explicar o funcionamento do **_Bucket Sort_**:
- Sua ideia geral se da com a criação de k baldes, sendo $k \leq n$
- Os valores do vetor são normalizados para cada valor cair no seu respectivo 
balde.
- Caso tenha mais de um valor presente em um balde é feita a ordenação por
comparação.
outros
- Tendo seu maior desempenho a ordenação de um vetor que está uniformemente distribuída.
$$ \text{balde[i]} =  \frac{vetor[i] - min(vetor)}{max(vetor) - min(vetor)}$$

##### b) Ordenar um vetor baseado no _Bucket Sort_:
    [7, 4, 15, 9, -1, 6, 17, 12, 3, 8] 
- Amplitude do vetor = max(vetor) - min(vetor)
- A quantidade de buckets será = n = 10
- buckets = [[], [], [], [], [], [], [], [], [], []]
- tamanho de um balde = round(amplitude/quantidade de baldes) = 2

- Primeira iteração(7): 
$$ index = \frac{7 - (-1)}{2}$$
$$ index = 4  $$
- buckets = [[], [], [], [], [7], [], [], [], [], []]

- Segunda iteração(4):
$$ index = \frac{4 - (-1)}{2}$$
$$ index = 2,5 $$
$$ index = 2 $$
- buckets = [[], [], [4], [], [7], [], [], [], [], []]

- Terceira iteração(15):
$$ index = \frac{15 - (-1)}{2}$$
$$ index = 8 $$
- buckets = [[], [], [4], [], [7], [], [], [], [15],[]]

- Quarta iteração(9):
$$ index = \frac{9 - (-1)}{2}$$
$$ index = 5 $$
- buckets = [[], [], [4], [], [7], [9], [], [], [15], []]

    [7, 4, 15, 9, -1, 6, 17, 12, 3, 8] 
- Quinta iteração(-1):
$$ index = \frac{-1 - (-1)}{2}$$
$$ index = 0 $$
- buckets = [[-1], [], [4], [], [7], [9], [], [], [15], []]

- Sexta iteração(6):
$$ index = \frac{6 - (-1)}{2}$$
$$ index = 3,5 $$
$$ index = 3 $$
- buckets = [[-1], [], [4], [6], [7], [9], [], [], [15], []]

- Setima iteração(17):
$$ index = \frac{17 - (-1)}{2}$$
$$ index = 2$$
- buckets = [[-1], [], [4], [6], [7], [9], [], [], [15], [17]]

- Oitava iteração(12):
$$ index = \frac{12 - (-1)}{2}$$
$$ index = 6,5$$
$$ index = 6$$
- buckets = [[-1], [], [4], [6], [7], [9], [12], [], [15], [17]]

- Nona iteração(3):
$$ index = \frac{3 - (-1)}{2}$$
$$ index = 2$$
- buckets = [[-1], [], [4, 3], [6], [7], [9], [12], [], [15], [17]]

- Decima iteração(8):
$$ index = \frac{8 - (-1)}{2}$$
$$ index = 4.5$$
$$ index = 4$$
- buckets = [[-1], [], [4, 3], [6], [7, 8], [9], [12], [], [15], [17]]

- Após a entrada de todos os valores nos seus respectivos baldes, ocorre a
ordenação por comparação por baldes:
- buckets = [[-1], [], [3, 4], [6], [7, 8], [9], [12], [], [15], [17]]

- E depois a concatenação dos valores em um único vetor de forma ordenada:

    ```[7, 4, 15, 9, -1, 6, 17, 12, 3, 8]```
### 5 - Questão 
- Calcular a complexidade do _**Bucket Sort**_
