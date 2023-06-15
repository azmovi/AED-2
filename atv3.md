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
        heapify(vector, i)```
