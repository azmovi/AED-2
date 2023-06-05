# Trabalho 2 - Levada 
    Nome: Antônio Cícero Amorim de Azevedo
    Ra: 811455 
###### Caso Médio:
- Representa o valor aproximado da complexidade de um algoritmo, quando ele é
ultizado na prática 

### 1 - Questão 
- Analise da complexidade do algoritmo de ordenação **_Bubble Sort_** para o
caso médio.

```py
def BubbleSort(vector):
    for i in range(len(vector)-1, -1, -1):
        for j in range(len(vector)):
            first, second = vector[j], vector[j+1]
            if  fist > second:
                fist, second = second, first #Swap
    return vector
```
###### Melhor Caso:
- O algoritimo nunca irá entrar no _IF Statement_ entretando ele continua
percorrendo os dois _loops_ presentes no codigo
$$
T(n) = \sum_{i=0}^{n-1}(\sum^{n-1}_{j=0}(1 + 3))
$$
$$
T(n) = \sum_{i =0}^{n-1}4*n
$$
$$
T(n) = n(4*n)
$$
$$
T(n) = 4*n^2
$$
$$
bigO(n^2)
$$

###### Pior Caso:

- Ao contrário do melhor caso, dessa vez o algoritmo ira entrar em todos os
_IF Statement_ 
$$
T(n) = \sum_{i=0}^{n-1}(\sum^{n-1}_{j=0}(1 + 5))
$$
$$
T(n) = \sum_{i =0}^{n-1}6*n
$$
$$
T(n) = n(6*n)
$$
$$
T(n) = 6*n^2
$$
$$
bigO(n^2)
$$

##### Conclusão:
Como o pior caso e o melhor caso tem o mesmo _bigO_ os casos intermediarios
tambem teram esse mesmo _bigO_, nesse caso _**n²**_.

$$
T(n) = \frac{1}{n} * \sum_{j=0}^{n-1}n^2
$$
$$
T(n) = \frac{1}{n} * n^3 
$$
$$
T(n) = n^2
$$
$$
bigO(n²)
$$

### 2 - Questão 
- Analise da complexidade do algoritmo de ordenação **_Insertion Sort_** para o
caso médio.

```py
def InsertionSort(vector):
    for i in range(2, len(vector)):
        pivot = i
        first = vector[pivot-1]
        second = vector[pivot]
        while (pivot > 1) and (second < first):
            first, second = second, first #Swap
            pivot -= 1
    return vector
```

- Para resolver o caso médio vou fazer o somátorio de todos os casos possíveis
dividido pela quantidade de casos
