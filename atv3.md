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

##### Árvore binária -> Heap (hepify):
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
