# Trabalho 2 - Levada 
    Nome: Antônio Cícero Amorim de Azevedo
    Ra: 811455 
###### Caso Médio:
- Representa o valor aproximado da complexidade de um algoritmo, quando ele é
utilizado na prática 

### 1 - Questão 
- Análise da complexidade do algoritmo de ordenação **_Bubble Sort_** para o
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
- O algoritmo nunca irá entrar no _IF Statement_ entretando ele continua
percorrendo os dois _loops_ presentes no código 
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

- Ao contrário do melhor caso, dessa vez o algoritmo irá entrar em todos os
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
Como o pior caso e o melhor caso tem o mesmo _bigO_ os casos intermediários
também terão esse mesmo _bigO_, nesse caso _**n²**_.

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
- Análise da complexidade do algoritmo **_Insertion Sort_** para o
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

- Para resolver o caso médio vou fazer o somatório de todos os casos possíveis
dividido pela quantidade de casos.
- Pior caso vai ocorrer n² interações (Vetor ordenado de forma decrescente) e
para o próximo caso apenas um valor estará na sua posição correta, logo n² - 1
interações.
$$
T(n) = \frac{1}{n}\sum_{i=0}^{n}(n^2- i)
$$
$$
\sum_{i=0}^{n}n^2- i = \sum_{i=0}^{n}n^2 - \sum_{i=0}^{n}i
$$
- Desenvolvendo o somatório:
$$
Sum = (n^2 + n^2 + ... + n^2) - (0 + 1 + 2+...+ n)
$$
- Soma de n² n vezes menos a soma de uma P.A de n termos
$$
Sum = n * n^2 - \frac{(1 + n)n}{2}
$$
$$
Sum = \frac{2n^3 - n^2 - n}{2}
$$
$$
Sum = \frac{n}{2} * (2n^2-n - 1)
$$
- Substituindo na função principal
$$
T(n) = \frac{1}{n} * \frac{n}{2} * (2n^2-n - 1)
$$
$$
T(n) = \frac{2n^2 - n - 1}{2}
$$
$$
T(n) = n^2 - \frac{n}{2} - \frac{1}{n}
$$

- Dessa forma percebemos que para o caso médio do _Insertion Sort_ será _O(n²)_.

### 3 - Questão 
- Análise da complexidade do **_Quick Sort_** no caso médio.

```py
def quick(vector, left, right):
    """  """
    if left < right:
        pivot = partition(vector, left, right)
        quick(vector, left, pivot-1) # Lado esquerdo
        quick(vector, pivot+1, right) # Lado direito

def partition(vector, left, right):
    """"""
    pivot = vector[right]
    atual = left - 1
    swap = left - 1
    while atual < right:
        atual += 1
        if vector[atual] <= pivot:
            swap += 1
            if atual > swap:
                vector[atual], vector[swap] = vector[swap], vector[atual]
    return swap
```
- Esse algoritmo utiliza a recursividade duas vezes por chamada de função, 
dessa forma para fazer o caso médio vamos supor que para a primeira chamada
recursiva ocorrerá o melhor caso e na segunda chamada ocorrerá o pior caso

###### Melhor caso (divisão balanceada):
- O pivô será próximo a média do vetor. A divisão irá retornar dois vetores de 
tamanhos parecidos ou iguais. 
$$ T(n) = n + T(\frac{n}{2}) + T(\frac{n}{2}) $$

###### Pior caso (divisão desbalanceada):
- O pivô será o maior número do vetor. A divisão irá retornar um único vetor.
$$ T(n) = n + T(n-1) + T(0) $$
###### Caso Médio:
- Para esse caso irei utilizar a ideia de alternar entre pior e melhor caso
$$ T(n) = n + 2T(\frac{n}{2}) $$
$$ T(n) = n + 2(\frac{n}{2} + T(\frac{n}{2} - 1)) $$
$$ T(n) = n + n + 2(\frac{n-2}{2} + 2T(\frac{n-2}{2})) $$
$$ T(n) = n + n + n - 2 + 4( \frac{n-2}{4} + T(\frac{n-2}{4} - 1)) $$

- Como podemos perceber a equação apresenta uma sequência bem definida
dada por:
$$ (2, 6, 14, 30, 62)= \sum_{i=1}^{k}2^i$$
$$ T(n) = 2(n *k - \sum_{i=1}^{k} 2^i) $$
$$ T(n) = 2(n *k - 2(2^k - 1)) $$

- Além do mais o critério de parada será quando:
$$ \frac{n - \sum_{i=1}^{k} 2^i}{2^k} = 1 $$

- Dessa forma chegamos em:
$$ n - \sum_{i=1}^{k} 2^i = 2^k $$

- Desenvolvendo o somatório da P.G e colocando na igualdade:
$$ 2^1 + 2^2 +... + 2^k = \frac{2(2^k - 1)}{2-1}  = 2^{k+1} - 2$$
$$ n - (2^{k+1} - 2)= 2^k $$
$$ n - 2^{k+1} + 2= 2^k $$
$$ n + 2= 2^k + 2^{k+1} $$
$$ n + 2= 2^k(1 + 2) $$
$$ n + 2= 2^k * 3$$
$$ \frac{n + 2}{3}= 2^k $$
$$ \log_{2}({\frac{n + 2}{3}})= \log2^k $$
$$ \log_{2}({\frac{n + 2}{3}})= k $$

- Substituindo o k na equação principal:
$$ T(n) = 2(n * \log_{2}({\frac{n + 2}{3}})- 2(2^{\log_{2}({\frac{n + 2}{3}})}
- 1)) $$
$$ T(n) = 2(n * log_{2}(n+2) - log_{2}3 - 2(\frac{n + 2}{3} - 1)) $$
$$ T(n) = 2(n * log_{2}(n+2) - log_{2}3 - 2(\frac{n + 2 - 3}{3}) $$
$$ T(n) = 2(n * log_{2}(n+2) - log_{2}3 - 2(\frac{n - 1}{3}) $$
$$ T(n) = 2(n * log_{2}(n+2) - log_{2}3 - \frac{2}{3}*(n - 1)) $$
$$ T(n) = 2n * log_{2}(n+2) - 2log_{2}3 - \frac{4}{3}*(n - 1) $$

- Removendo constantes que serão desprezíveis para n(s) muito grandes:
$$ T(n) = n * log_{2}(n) - n $$

- Dessa forma percebemos que o BigO do **_Quick Sort_** será:
$$ O(n*log_{2}n) $$


    
### 4 - Questão 
- Análise da complexidade do **_Shell Sort_** no caso médio.
- Um variação do Insertion Sort, baseada em gaps (n/2, n/4, ..., 1)

```py
def ShellSort(vector):
    gap = len(vector)//2
    while gap > 0:
        for i in range(gap, len(vector) - 1):
            j = i
            first = j-gap
            second = j
            while j >= gap and vector[first] > vector[second]:
                vector[first], vector[second] = vector[second], vector[first] 
                j -= gap
        gap //= 2
```
###### Pior caso:
- O vetor estará organizado de forma decrescente. Dessa forma ela entrada nos
dois loops a mesma quantidade de vezes logo:
$$ T(n) = 2(n - \frac{n}{2}) + 4(n - \frac{n}{4}) + ... + 2^k(n - \frac{n}{2^k}) $$

- Condição de parada.
$$ \frac{n}{2^k} = 1$$
$$ n = 2^k $$
$$ \log_{2} n = k  *\log_{2}2 $$
$$ \log_{2} n = k  $$


###### Caso Médio:
- Para calcular esse caso, vamos supor que o loop só irá realizar metade das
trocas possíveis dentro de uma iteração.
- Dessa forma baseando na equação do pior entrando dividindo por dois
$$ T(n) = \frac{2}{2}(n - \frac{n}{2}) + \frac{4}{2}(n - \frac{n}{4}) + ... + 
\frac{2^k}{2}(n - \frac{n}{2^k}) $$

- Simplificando:
$$ T(n) = (n - \frac{n}{2}) + 2(n - \frac{n}{4}) +.. + 2^{k-1}(n - \frac{n}{2^k}) $$
$$ T(n) = n - \frac{n}{2} + 2n - \frac{2n}{4} +...+ 2^{k-1}n - \frac{2^{k-1}n}{2^k}$$
$$ T(n) = n - \frac{n}{2} + 2n - \frac{n}{2} +...+ 2^{k-1}n - \frac{n}{2}$$
$$ T(n) = n + 2n +...+ 2^{k-1}n  - \frac{nk}{2} $$
$$ T(n) = n\sum_{i=0}^{k-1}2^i  - \frac{nk}{2} $$
$$ T(n) = n(\sum_{i=0}^{k-1}2^i  - \frac{k}{2}) $$
$$ T(n) = n(\frac{1(2^{k-1} - 1)}{2 - 1} - \frac{k}{2}) $$
$$ T(n) = n(2^{k-1} - 1 - \frac{k}{2}) $$
$$ T(n) = n(\frac{2^k}{2} - 1 - \frac{k}{2}) $$

- Substituindo _k_ = $\log_{2}n$:
$$ T(n) = n(\frac{2^{\log_{2}n}}{2} - 1 - \frac{\log_{2}n}{2}) $$
$$ T(n) = \frac{n *2^{\log_{2}n}}{2} - n - \frac{n\log_{2}n}{2} $$

- Removendo valores constantes que são indiferentes para a complexidade assintótica.

$$ T(n) = n *n - n - n\log_{2}n $$
$$ T(n) = n^2 - n - n\log_{2}n $$

- Dessa formas conseguimos perceber que o _BigO_ do shell sort no caso médio será:
$$ O(n^2) $$


### 5 - Questão 
- Análise da complexidade do Merge Sort, para os três possíveis casos>
    - Melhor caso
    - Pior caso
    - Caso médio

```py
def mergeSort(vector):
    """ Divide """
    if len(vector) > 1:
        mid = len(vector)//2
        left = vector[:mid]
        right = vector[mid:]

        left = mergeSort(left)
        right = mergeSort(right)

        return merge(left, right)

    return vector

def merge(left, right):
    """ Compara e Aglutina """
    ordenado = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ordenado.append(left[i])
            i += 1
        else:
            ordenado.append(right[j])
            j += 1

    ordenado += left[i:] 
    ordenado += right[j:] 
    return ordenado
```
###### Análise da complexidade
- Primeira etapa é a divisão do vetor até formar vários sub vetores de tamanho um.
- Segunda etapa é a comparação entre os sub vetores de elementos únicos.
- Terceira etapa é a aglutinação dos sub vetores ordenados.

$$ T(n) = 1 + T(\frac{n}{2}) + T(\frac{n}{2}) + 2 + 2 \frac{n}{2} + 2 $$

- Removendo constantes e simplificando:
$$ T(n) = 2T(\frac{n}{2}) + n $$

- Expandido a recursividade
$$ T(n) = 2(2T(\frac{n}{4}) + 2{\frac{n}{4}} )+ n $$
$$ T(n) = 2(2T(\frac{n}{4}) + \frac{n}{2} )+ n $$
$$ T(n) = 4T(\frac{n}{4}) + 2\frac{n}{2} + n$$
$$ T(n) = 2^2T(\frac{n}{2^2}) + 2n$$
 - Generalizando...
 $$T(n) =  2^kT(\frac{n}{2^k}) + kn$$

 - Critério de parada:
$$ T(\frac{n}{2^k}) = ? $$
$$ \frac{n}{2^k} = 1 $$
$$ n = 2^k $$
$$ \log_{2}n = \log_{2}2^k $$
$$ \log_{2}n = k * \log_{2}2 $$
$$ \log_{2}n = k $$

- Substituindo na equação principal:
 $$T(n) =  2^kT(\frac{n}{2^k}) + kn$$
 $$T(n) =  2^{\log_{2}n}*T(1) + \log_{2}n *n$$
 $$T(n) =  \log_{2}n*T(1) + \log_{2}n *n$$

 - Simplificando:

 $$T(n) =  \log_{2}n + \log_{2}n * n$$

- Dessa formas conseguimos perceber que o _BigO_ do Merge Sort será:
$$ O(n \log_{2}{n}) $$

- Esse tempo de complexidade será igual para todos os casos, devido ao fato das
divisões de vetor serem feitas antes da comparação.
- Dessa forma até um vetor ordenado terá um tempo de $O(n \log_{2}{n})$ dentro
do _**Merge Sort**_.
