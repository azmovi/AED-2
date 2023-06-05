# Trabalho 2 - Levada 
```
Nome: Antônio Cícero Amorim de Azevedo
Ra: 811455 
``` 

### 1 - Questão 
#### Caso Médio:
- soma de todos os casos possíveis dividido pela sua quantidade de casos 
- algoritmo de ordenação **_bubblesort_**
```py
def bubble(vector):
    for i in range(len(vector)-1, -1, -1):
        for j in range(len(vector)):
            first, second = vector[j], vector[j+1]
            if  fist > second:
                fist, second = second, first # Swap
```
###### Melhor Caso:
- O algoritimo nunca irá entrar no _IF Statement_ entretando ele continua
percorrendo os dois _loops_ presentes no codigo
$$
T(n) = \sum_{i=0}^{n}(\sum^{n}_{j=0}(1 + 3))
$$
$$
T(n) = \sum_{i =0}^{n}4*n
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
     O 1 representa o primeiro for 
     O 3 representa a declaração das variaveis + o segundor for 


###### Pior Caso:

- Ao contrário do melhor caso, dessa vez o algoritmo ira entrar em todos os
_IF Statement_ 
$$
T(n) = \sum_{i=0}^{n}(\sum^{n}_{j=0}(1 + 5))
$$
$$
T(n) = \sum_{i =0}^{n}6*n
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
tambem teram esse mesmo _bigO_, no caso especifico n².
$$

