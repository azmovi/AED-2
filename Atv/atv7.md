# Trabalho 7 - Levada 
    Nome: Antônio Cícero Amorim de Azevedo
    Ra: 811455 
> Tabela de Espalhamento(_hash table_)

### 1 - Questão 
Provar que a complexidade do caso médio para busca de chaves é igual a $O(1 + \alpha)$
sabendo que $\alpha = \frac{n}{m}$:


- $n$ representa nosso número total de chaves e m representa o número de slots
disponíveis com a função hash.

- Devemos ter em mente que a complexidade da função hash é igual a $O(1)$ pois
representa apenas uma sequencia de cálculos matemáticos.

- Outro ponto é que caso duas ou mais chaves tenha o mesmo valor de hash, esses
valores estarão se relacionando através de uma lista ligada.

###### Conclusão:
$$T(n) = \text{calculo do hash} + \text{busca na lista ligada}$$

- Calculo do Hash será $O(1)$

- Busca na lista ligada será $\frac{n}{m}$, que representa a média de elementos
por um slot relacionado a um hash.

$$T(n) = O(1) + O(\frac{n}{m}) $$

- Substituindo por $\alpha$ concluimos que a complexidade média será:

$$T(n) = O(1) + O(\alpha) $$
$$O(1 + \alpha)$$

### 2 - Questão 
Dado 4 funções hash qual deles desempenha o melhor para m = 10:
1. h(i) = $i^2 \space \% \space m$
2. h(i) = $i^3 \space \% \space m$
3. h(i) = $(11 * i^2) \space \% \space m$
4. h(i) = $(12 * i) \space \% \space m$

#### Para $h(i) = i^2 \space \% \space m$
###### Primeira operação

hash = [[], [], [], [], [], [], [], [], [], []]

$h(0) = 0^2 \space \% \space 10$

h(0) = 0

hash = [[0], [], [], [], [], [], [], [], [], []]

###### Segunda operação

$h(1) = 1^2 \space \% \space 10$

h(1) = 1 

hash = [[0], [1], [], [], [], [], [], [], [], []]

###### Terceira operação

$h(2) = 2^2 \space \% \space 10$

h(2) = 4

hash = [[0], [1], [], [], [2], [], [], [], [], []]

###### Quarta operação

$h(3) = 3^2 \space \% \space 10$

h(3) = 9

hash = [[0], [1], [], [], [2], [], [], [], [], [9]]

###### Quinta operação

$h(4) = 4^2 \space \% \space 10$

h(4) = 6

hash = [[0], [1], [], [], [2], [], [4], [], [], [9]]

###### Sexta operação

$h(5) = 5^2 \space \% \space 10$

h(5) = 5

hash = [[0], [1], [], [], [2], [5], [4], [], [], [9]]

###### Sétima operação

$h(6) = 6^2 \space \% \space 10$

h(6) = 6

hash = [[0], [1], [], [], [2], [5], [4, 6], [], [], [9]]

###### Oitava operação

$h(7) = 7^2 \space \% \space 10$

h(7) = 9

hash = [[0], [1], [], [], [2], [5], [4, 6], [], [], [9, 7]]

###### Nona operação

$h(8) = 8^2 \space \% \space 10$

h(8) = 4

hash = [[0], [1], [], [], [2, 8], [5], [4, 6], [], [], [9, 7]]

###### Decima operação

$h(9) = 9^2 \space \% \space 10$

h(9) = 1

hash = [[0], [1, 9], [], [], [2, 8], [5], [4, 6], [], [], [9, 7]]

#### Para $h(i) = i^3 \space \% \space m$

hash = [[], [], [], [], [], [], [], [], [], []]

###### Primeira operação

$h(0) = 0^3 \space \% \space 10$

h(0) = 0

hash = [[0], [], [], [], [], [], [], [], [], []]

###### Segunda operação

$h(1) = 1^3 \space \% \space 10$

h(1) = 1 

hash = [[0], [1], [], [], [], [], [], [], [], []]

###### Terceira operação

$h(2) = 2^3 \space \% \space 10$

h(2) = 8

hash = [[0], [1], [], [], [], [], [], [], [2], []]

###### Quarta operação

$h(3) = 3^3 \space \% \space 10$

h(3) = 7

hash = [[0], [1], [], [], [], [], [], [3], [2], []]

###### Quinta operação

$h(4) = 4^3 \space \% \space 10$

h(4) = 4

hash = [[0], [1], [], [], [4], [], [], [3], [2], []]

###### Sexta operação

$h(5) = 5^3 \space \% \space 10$

h(5) = 5

hash = [[0], [1], [], [], [4], [5], [], [3], [2], []]

###### Sétima operação

$h(6) = 6^3 \space \% \space 10$

h(6) = 6

hash = [[0], [1], [], [], [4], [5], [6], [3], [2], []]

###### Oitava operação

$h(7) = 7^3 \space \% \space 10$

h(7) = 3

hash = [[0], [1], [], [7], [4], [5], [6], [3], [2], []]

###### Nona operação

$h(8) = 8^3 \space \% \space 10$

h(8) = 2

hash = [[0], [1], [2], [7], [4], [5], [6], [3], [2], []]

###### Decima operação

$h(9) = 9^3 \space \% \space 10$

h(9) = 9

hash = [[0], [1], [2], [7], [4], [5], [6], [3], [2], [9]]

#### Para $h(i) = (11 * i^2) \space \% \space m$

hash = [[], [], [], [], [], [], [], [], [], []]

###### Primeira operação

$h(0) = (11 * 0^2) \space \% \space 10$

h(0) = 0

hash = [[0], [], [], [], [], [], [], [], [], []]

###### Segunda operação

$h(1) = (11 * 1^2) \space \% \space 10$

h(1) = 1 

hash = [[0], [1], [], [], [], [], [], [], [], []]

###### Terceira operação

$h(2) = (11 * 2^2) \space \% \space 10$

h(2) = 4

hash = [[0], [1], [], [], [2], [], [], [], [], []]

###### Quarta operação

$h(3) = (11 * 3^2) \space \% \space 10$

h(3) = 9

hash = [[0], [1], [], [], [2], [], [], [], [], [3]]

###### Quinta operação

$h(4) = (11 * 4^2) \space \% \space 10$

h(4) =  6

hash = [[0], [1], [], [], [2], [], [4], [], [], [3]]

###### Sexta operação

$h(5) = (11 * 5^2) \space \% \space 10$

h(5) = 5

hash = [[0], [1], [], [], [2], [5], [4], [], [], [3]]

###### Sétima operação

$h(6) = (11 * 6^2) \space \% \space 10$

h(6) = 6

hash = [[0], [1], [], [], [2], [5], [4, 6], [], [], [3]]

###### Oitava operação

$h(7) = (11 * 7^2) \space \% \space 10$

h(7) = 9

hash = [[0], [1], [], [], [2], [5], [4, 6], [], [], [3, 7]]

###### Nona operação

$h(8) = (11 * 8^2) \space \% \space 10$

h(8) = 4

hash = [[0], [1], [], [], [2, 8], [5], [4, 6], [], [], [3, 7]]

###### Decima operação

$h(9) = (11 * 9^2) \space \% \space 10$

h(9) = 1

hash = [[0], [1, 9], [], [], [2, 8], [5], [4, 6], [], [], [3, 7]]

#### Para $h(i) = (12 * i) \space \% \space m$

hash = [[], [], [], [], [], [], [], [], [], []]

###### Primeira operação

$h(0) = (12 * 0) \space \% \space 10$

h(0) = 0

hash = [[0], [], [], [], [], [], [], [], [], []]

###### Segunda operação

$h(1) = (12 * 1) \space \% \space 10$

h(1) = 2 

hash = [[0], [], [1], [], [], [], [], [], [], []]

###### Terceira operação

$h(2) = (12 * 2) \space \% \space 10$

h(2) = 4

hash = [[0], [], [1], [], [2], [], [], [], [], []]

###### Quarta operação

$h(3) = (12 * 3) \space \% \space 10$

h(3) = 6

hash = [[0], [], [1], [], [2], [], [3], [], [], []]

###### Quinta operação

$h(4) = (12 * 4) \space \% \space 10$

h(4) =  8

hash = [[0], [], [1], [], [2], [], [3], [], [4], []]

###### Sexta operação

$h(5) = (12 * 5) \space \% \space 10$

h(5) = 0

hash = [[0, 5], [], [1], [], [2], [], [3], [], [4], []]

###### Sétima operação

$h(6) = (12 * 6) \space \% \space 10$

h(6) = 2

hash = [[0, 5], [], [1, 6], [], [2], [], [3], [], [4], []]

###### Oitava operação

$h(7) = (12 * 7) \space \% \space 10$

h(7) = 4

hash = [[0, 5], [], [1, 6], [], [2, 4], [], [3], [], [4], []]

###### Nona operação

$h(8) = (12 * 8) \space \% \space 10$

h(8) = 6

hash = [[0, 5], [], [1, 6], [], [2, 4], [], [3, 8], [], [4], []]

###### Decima operação

$h(9) = (12 * 9) \space \% \space 10$

h(9) = 8

hash = [[0, 5], [], [1, 6], [], [2, 4], [], [3, 8], [], [4, 9], []]


##### Conclusão:
Vetores após as operações de hashing:

1. [[0], [1, 9], [], [], [2, 8], [5], [4, 6], [], [], [9, 7]]
2. [[0], [1], [2], [7], [4], [5], [6], [3], [2], [9]]
3. [[0], [1, 9], [], [], [2, 8], [5], [4, 6], [], [], [3, 7]]
4. [[0, 5], [], [1, 6], [], [2, 4], [], [3, 8], [], [4, 9], []]

Como podemos perceber a equação $h(i) = i^3 \space \% \space m$ foi a que apresentou
o menor número de colisões, ou seja, números que apresentam o mesmo hash, dessa forma
essa é a melhor resolve o problema.

### 3 - Questão 
Considerando uma tabela hashing simples uniforme, onde $\alpha < 1$, o número de 
sondagens esperado na busca é de no máximo $\frac{1}{\alpha} * \ln{\frac{1}{1-\alpha}}$

- Tendo em mente que o valor esperado para uma sondagem é:
$$ E[X_i] \leq \frac{1}{1-\alpha_i}$$


- Chegamos na média igual a:
$$ \frac{1}{n} \sum_{i=0}^{n-1}E[X_{i}]$$
$$ \frac{1}{n} \sum_{i=0}^{n-1} \frac{1}{1-\alpha_i}$$
$$ \frac{1}{n} \sum_{i=0}^{n-1} \frac{1}{1-\frac{i}{m}}$$
$$ \frac{1}{n} \sum_{i=0}^{n-1} \frac{m}{i-m}$$
$$ \frac{m}{n} \sum_{i=0}^{n-1} \frac{1}{i-m}$$
$$ \frac{1}{\alpha} \sum_{i=0}^{n-1} \frac{1}{i-m}$$

- Considerando $k = m-i$
$$ \frac{1}{\alpha} \sum_{i=0}^{n-1} \frac{1}{k}$$

$i = 0 \rightarrow k = m$

$i = n - 1 \rightarrow k = m - n + 1$

$$ \frac{1}{\alpha} \sum_{k = m - n + 1}^{m} \frac{1}{k}$$

- Podemos fazer uma aproximação para a integral:
$$ \frac{1}{\alpha} \int_{m-n}^{m} \frac{1}{x} dx$$
$$ \int_{m-n}^{m} \frac{1}{x} dx = \ln{x} + C $$
$$ \frac{1}{\alpha} \ln{x} \mid_{m-n}^{m} $$
$$ \frac{1}{\alpha} (\ln{m} - \ln({m-n})) $$

- Simplificando ficamos com:
$$ \frac{1}{\alpha} \ln{\frac{m}{m-n}} $$
$$ \frac{1}{\alpha} \ln{\frac{1}{\frac{m-n}{m}}} $$
$$ \frac{1}{\alpha} \ln{\frac{1}{1 - \frac{n}{m}}} $$

$$ \frac{1}{\alpha} \ln{\frac{1}{1 - \alpha}} $$

### 4 - Questão 
Fazer a inserção de $10, 22, 31, 4, 15, 28, 17, 88, 59$, dada uma tabela de espalhamento
de tamanho igual 11 utilizando os 3 métodos de endereçamento aberto, com a função
auxiliar sendo $h'(k) = k$

###### A) Sondagem linear:
hash = [[], [], [], [], [], [], [], [], [], [], [], []]

$h(k,i) = (h'(k) + i) \space \% \space m$

- Inserir valor 10

$h(10,0) = (h'(10) + 0) \space \% \space 11$

$h(10,0) = 10$

hash = [[], [], [], [], [], [], [], [], [], [], [], [10]]

- Inserir valor 22 

$h(22,0) = (h'(22) + 0) \space \% \space 11$

$h(22,0) = 0$

hash = [[22], [], [], [], [], [], [], [], [], [], [], [10]]

- Inserir valor 31

$h(31,0) = (h'(31) + 0) \space \% \space 11$

$h(31,0) = 9$

hash = [[22], [], [], [], [], [], [], [], [], [], [31], [10]]

- Inserir valor 4

$h(4,0) = (h'(4) + 0) \space \% \space 11$

$h(4,0) = 4$

hash = [[22], [], [], [], [4], [], [], [], [], [], [31], [10]]
- Inserir valor 15

$h(15,0) = (h'(15) + 0) \space \% \space 11$

$h(15,0) = 4$

$h(15,1) = (h'(15) + 1) \space \% \space 11$

$h(15,1) = 5$

hash = [[22], [], [], [], [4], [15], [], [], [], [], [31], [10]]

- Inserir valor 28

$h(28,0) = (h'(28) + 0) \space \% \space 11$

$h(28,0) = 6$

hash = [[22], [], [], [], [4], [15], [28], [], [], [], [31], [10]]

- Inserir valor 17

$h(17,0) = (h'(17) + 0) \space \% \space 11$

$h(17,0) = 6$

$h(17,1) = (h'(17) + 1) \space \% \space 11$

$h(17,1) = 7$

hash = [[22], [], [], [], [4], [15], [28], [17], [], [], [31], [10]]

- Inserir valor 88

$h(88,0) = (h'(88) + 0) \space \% \space 11$

$h(88,0) = 0$

$h(88,1) = (h'(88) + 1) \space \% \space 11$

$h(88,1) = 1$

hash = [[22], [88], [], [], [4], [15], [28], [17], [], [], [31], [10]]

- Inserir valor 59

$h(59,0) = (h'(59) + 0) \space \% \space 11$

$h(59,0) = 4$

$h(59,1) = (h'(59) + 1) \space \% \space 11$

$h(59,1) = 5$

$h(59,2) = (h'(59) + 2) \space \% \space 11$

$h(59,2) = 6$

$h(59,3) = (h'(59) + 3) \space \% \space 11$

$h(59,3) = 7$

$h(59,4) = (h'(59) + 4) \space \% \space 11$

$h(59,4) = 8$

hash = [[22], [88], [], [], [4], [15], [28], [17], [59], [], [31], [10]]

###### B) Sondagem quadrática:

$h(k, i) = (h'(k) + c_{1}i + c_{2}i^2) \space \% \space m$

- Inserir valor 10

$h(10, 0) = (h'(10) + 0 + 0^2) \space \% \space 10$

$h(10,0) = 10$

hash = [[], [], [], [], [], [], [], [], [], [], [], [10]]

- Inserir valor 22 

$h(22, 0) = (h'(22) + 0 + 0^2) \space \% \space 11$

$h(22,0) = 0$

hash = [[22], [], [], [], [], [], [], [], [], [], [], [10]]

- Inserir valor 31

$h(31, 0) = (h'(31) + 0 + 0^2) \space \% \space 11$

$h(31,0) = 9$

hash = [[22], [], [], [], [], [], [], [], [], [], [31], [10]]

- Inserir valor 4

$h(4, 0) = (h'(4) + 0 + 0^2) \space \% \space 11$

$h(4,0) = 4$

hash = [[22], [], [], [], [4], [], [], [], [], [], [31], [10]]
- Inserir valor 15

$h(15, 0) = (h'(15) + 0 + 0^2) \space \% \space 11$

$h(15,0) = 4$

$h(15, 1) = (h'(15) + 1 + 1^2) \space \% \space 11$

$h(15,1) = 6$

hash = [[22], [], [], [], [4], [], [15], [], [], [], [31], [10]]

- Inserir valor 28

$h(28, 0) = (h'(28) + 0 + 0^2) \space \% \space 11$

$h(28, 0) = 6$

$h(28, 1) = (h'(28) + 1 + 1^2) \space \% \space 11$

$h(28, 1) = 10$

$h(28, 2) = (h'(28) + 2 + 2^2) \space \% \space 11$

$h(28, 2) = 3$

hash = [[22], [], [], [28], [4], [], [15], [], [], [], [31], [10]]

- Inserir valor 17

$h(17, 0) = (h'(17) + 0 + 0^2) \space \% \space 11$

$h(17,0) = 6$

$h(17, 1) = (h'(17) + 1 + 1^2) \space \% \space 11$

$h(17, 1) = 8$

hash = [[22], [], [], [28], [4], [], [15], [], [17], [], [31], [10]]

- Inserir valor 88

$h(88, 0) = (h'(88) + 0 + 0^2) \space \% \space 11$

$h(88, 0) = 0$

$h(88, 1) = (h'(88) + 1 + 1^2) \space \% \space 11$

$h(88, 1) = 2$

hash = [[22], [], [88], [28], [4], [], [15], [], [17], [], [31], [10]]

- Inserir valor 59

$h(59, 0) = (h'(59) + 0 + 0^2) \space \% \space 11$

$h(59,0) = 4$

$h(59, 1) = (h'(59) + 1 + 1^2) \space \% \space 11$

$h(59, 1) = 6$

$h(59, 2) = (h'(59) + 2 + 2^2) \space \% \space 11$

$h(59, 2) = 10$

$h(59, 3) = (h'(59) + 3 + 3^2) \space \% \space 11$

$h(59, 3) = 5$

hash = [[22], [], [88], [28], [4], [59], [15], [], [17], [], [31], [10]]

###### C) Duplo espalhamento

$h(k, i) = (h_{1}(k) + i*h_{2}(k)) \space \% \space m$

$h_{1}(k) = k \space \% \space m$
$h_{2}(k) = 1 + (k \space \% \space 7)$

- Inserir valor 10

$h(10, 0) = (h_{1}(10) + 0*h_{2}(22)) \space \% \space 11$

$h(10,0) = 10$

hash = [[], [], [], [], [], [], [], [], [], [], [], [10]]

- Inserir valor 22 

$h(22, 0) = (h_{1}(22) + 0*h_{2}(22)) \space \% \space 11$

$h(22,0) = 0$

hash = [[22], [], [], [], [], [], [], [], [], [], [], [10]]

- Inserir valor 31

$h(31, 0) = (h_{1}(31) + 0*h_{2}(31)) \space \% \space 11$

$h(31,0) = 9$

hash = [[22], [], [], [], [], [], [], [], [], [], [31], [10]]

- Inserir valor 4

$h(4, 0) = (h_{1}(4) + 0*h_{2}(4)) \space \% \space 11$

$h(4,0) = 4$

hash = [[22], [], [], [], [4], [], [], [], [], [], [31], [10]]
- Inserir valor 15

$h(15, 0) = (h_{1}(15) + 0*h_{2}(15)) \space \% \space 11$

$h(15, 0) = 4$

$h(15, 1) = (h_{1}(15) + 1*h_{2}(15)) \space \% \space 11$
$h(15, 1) = 5$

hash = [[22], [], [], [], [4], [15], [], [], [], [], [31], [10]]

- Inserir valor 28

$h(28, 0) = (h_{1}(28) + 0*h_{2}(28)) \space \% \space 11$

$h(28, 0) = 6$

hash = [[22], [], [], [], [4], [15], [28], [], [], [], [31], [10]]

- Inserir valor 17

$h(17, 0) = (h_{1}(17) + 0*h_{2}(17)) \space \% \space 11$

$h(17,0) = 6$

$h(17, 1) = (h_{1}(17) + 1*h_{2}(17)) \space \% \space 11$

$h(17, 1) = 9$

$h(17, 2) = (h_{1}(17) + 2*h_{2}(17)) \space \% \space 11$

$h(17, 2) = 1$

hash = [[22], [17], [], [], [4], [15], [28], [], [], [], [31], [10]]

- Inserir valor 88

$h(88, 0) = (h_{1}(88) + 0*h_{2}(88)) \space \% \space 11$

$h(88, 0) = 0$

$h(88, 1) = (h_{1}(88) + 1*h_{2}(88)) \space \% \space 11$

$h(88, 1) = 4$

$h(88, 2) = (h_{1}(88) + 2*h_{2}(88)) \space \% \space 11$

$h(88, 2) = 8$

hash = [[22], [17], [], [], [4], [15], [28], [], [], [88], [31], [10]]

- Inserir valor 59

$h(59, 0) = (h_{1}(59) + 0*h_{2}(59)) \space \% \space 11$

$h(59, 0) = 4$

$h(59, 1) = (h_{1}(59) + 1*h_{2}(59)) \space \% \space 11$

$h(59, 7) = 7$

hash = [[22], [], [88], [28], [4], [59], [15], [], [17], [59], [31], [10]]


### 5 - Questão 
Dado $p = 97, \space a = 64, \space b = 7$ Crie a hash table baseada na estrategia
de hashing perfeito para as chaves $k = [9, 23, 37, 76, 62, 14, 85, 59, 17, 3]$.

- Dada a função de hashing perfeito:
$$h_{j}(k)  = ((k * a_{j} + b_{j}) \space \% \space p) \space \% \space m_{j}$$

hash = [[], [], [], [], [], [], [], [], [], [], []]

- Inserir valor 9 

$h(9)  = ((9 * 64 + 7) \space \% \space 97) \space \% \space 10$

$h(9) = 1$

hash = [[], [9], [], [], [], [], [], [], [], [], []]

- Inserir valor 23

$h(23)  = ((23 * 64 + 7) \space \% \space 97) \space \% \space 10$

$h(23) = 4$

hash = [[], [9], [], [], [23], [], [], [], [], [], []]

- Inserir valor 37

$h(37)  = ((37 * 64 + 7) \space \% \space 97) \space \% \space 10$

$h(37) = 7$

hash = [[], [9], [], [], [23], [], [], [37], [], [], []]

- Inserir valor 76

$h(76)  = ((76 * 64 + 7) \space \% \space 97) \space \% \space 10$

$h(76) = 1$

hash = [[], [9, 76], [], [], [23], [], [], [37], [], [], []]

- Inserir valor 62

$h(62)  = ((62 * 64 + 7) \space \% \space 97) \space \% \space 10$

$h(62) = 5$

hash = [[], [9, 76], [], [], [23], [62], [], [37], [], [], []]

- Inserir valor 14

$h(14)  = ((14 * 64 + 7) \space \% \space 97) \space \% \space 10$

$h(14) = 0$

hash = [[14], [9, 76], [], [], [23], [62], [], [37], [], [], []]

- Inserir valor 85

$h(85)  = ((85 * 64 + 7) \space \% \space 97) \space \% \space 10$

$h(85) = 5$

hash = [[14], [9, 76], [], [], [23], [62, 85], [], [37], [], [], []]

- Inserir valor 59

$h(59)  = ((59 * 64 + 7) \space \% \space 97) \space \% \space 10$

$h(59) = 0$

hash = [[14, 59], [9, 76], [], [], [23], [62, 85], [], [37], [], [], []]

- Inserir valor 17

$h(17)  = ((17 * 64 + 7) \space \% \space 97) \space \% \space 10$

$h(17) = 8$

hash = [[14, 59], [9, 76], [], [], [23], [62, 85], [], [37], [17], [], []]

- Inserir valor 3 

$h(3)  = ((3 * 64 + 7) \space \% \space 97) \space \% \space 10$

$h(3) = 5$

hash = [[14, 59], [9, 76], [], [], [23], [62, 85, 3], [], [37], [17], [], []]

- Apos a inserção inicial devemos checar se:
$$\sum_{j=0}^{m-1} n_{j}^2 < 2n$$
$$ 4 + 4 + 0 + 0 + 1 + 9 + 0 + 1 + 1 + 0 + 0 = 20$$
$$ 20 < 2 * 10 \text(False) $$ 

###### Calculo do hash para $[14, 59]$:
$m = 4, a = 14, b = 59$

- Hashing no valor 14 

$h'(14)  = ((14 * 14 + 59) \space \% \space 97) \space \% \space 4$

$h'(14) = 1$

hash = [[[], [14], [], []], [9, 76], [], [], [23], [62, 85, 3], [], [37], [17], [], []]

- Hashing no valor 59 

$h'(59)  = ((14 * 59 + 59) \space \% \space 97) \space \% \space 4$

$h'(59) = 0$

hash = [[[59], [14], [], []], [9, 76], [], [], [23], [62, 85, 3], [], [37], [17], [], []]

###### Calculo do hash para $[9, 79]$:
$m = 4, a = 9, b = 79$

- Hashing no valor 9 

$h'(9)  = ((9 * 9+ 79) \space \% \space 97) \space \% \space 4$

$h'(9) = 3$

hash = [[[], [14], [], []], [[], [], [], [9]], [], [], [23], [62, 85, 3], [], [37], [17], [], []]

- Hashing no valor 79

$h'(79)  = ((79 * 9 + 79) \space \% \space 97) \space \% \space 4$

$h'(79) = 2$

hash = [[[], [14], [], []], [[], [], [79], [9]], [], [], [23], [62, 85, 3], [], [37], [17], [], []]

###### Calculo do hash para $[62, 85, 3]$:
$m = 9, a = 62, b = 85$

- Hashing no valor 62

$h'(62)  = ((62 * 62 + 85) \space \% \space 97) \space \% \space 9$

$h'(62) = 4$

hash = [[[], [14], [], []], [[], [], [], [9]], [], [], [23], [[], [], [], [], [62], [], [], [], [], []], [], [37], [17], [], []]

- Hashing no valor 85

$h'(85)  = ((85 * 62 + 85) \space \% \space 97) \space \% \space 9$

$h'(85) = 2$

hash = [[[], [14], [], []], [[], [], [], [9]], [], [], [23], [[], [], [85], [], [62], [], [], [], [], []], [], [37], [17], [], []]

- Hashing no valor 3

$h'(3)  = ((3 * 62 + 85) \space \% \space 97) \space \% \space 9$

$h'(3) = 5$

hash = [[[], [14], [], []], [[], [], [], [9]], [], [], [23], [[], [], [85], [], [62], [3], [], [], [], []], [], [37], [17], [], []]


