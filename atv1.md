
# Trabalho 1 - Levada 
```
Nome: Antônio Cícero Amorim de Azevedo
Ra: 811455 
``` 
### 1 - Questão
A notação big-O é responsável por descrever o crescimento temporal de um algoritmo
em relação ao tamanho de entrada da função
- Em termos matemáticos:
$$
f(n) = O(g(n))
$$
- Tal que exista uma constante positiva $c$ e $n_{0}$ onde:
$$ 
f(n) \leq c \cdotp g(n) 
$$
- Para todo $n \leq n_{0}$

### 2 - Questão
Provar que essa igualdade é verdadeira:
$$
\sum_{k=1}^n = x_{k+1} - x_{1}
$$
- Abstraindo
$$
\sum_{k=1}^n = \sum_{k=1}^n x_{k+1} -\sum_{k=1}^n x_{k}
$$
$$
=(x_{1+1} + x_{2 + 1} ... + x_{(n-2)+1} +x_{(n-1)+1} + x_{n + 1}) - (x_1 + x_2 +x_3... + x_{n -1}+ x_{n})
$$
$$
=x_{2} + x_{3} ... +x_{n-1} +x_{n} + x_{n + 1} - x_1 - x_2 - x_3... - x_{n -1}- x_{n}
$$
- Cancelando os valores de forma telescópica ficamos com:
$$
= x_{n+1} - x_1
$$
 Validando a proposta inicial.


### 3 - Questão
```py
def Algo_C(n):
    a = 100
    j, k = n, 0
    while j > 0:
        while k < j:
            a += a
            k += 1
        j -= 1
        k = 0
    return a
```
Encontrar o número de operações executadas por essa função e mostrar sua complexidade
- Número de Operações:
$$
t(n) = 1 + 2 + \sum_{j=0}^n(\sum_{k=0}^{j+1}(2k)+2)
$$
- Expandindo a equação:
$$
t(n) = 3 + \sum_{j=0}^n\sum_{k=0}^{j+1}2k + \sum_{j=0}^n2
$$
- Expansão do duplo somatório:
$$
\sum_{j=0}^n\sum_{k=0}^{j+1}2k = 2*0 + 2*1+2*2... +2*(n-1) + 2*n
$$
- Dessa forma pode-se observar a soma de n termos de uma P.A de razão  = 2
$$
\sum_{j=0}^n\sum_{k=0}^{j+1}2k = \frac{(0+2n)n}{2}
$$
$$
\sum_{j=0}^n\sum_{k=0}^{j+1}2k = \frac{2n^2}{2}
$$
$$
\sum_{j=0}^n\sum_{k=0}^{j+1}2k = n²
$$
Substituindo na equação geral e chegando nesse forma reduzida:
$$
t(n) = 3 + n^2 + 2n
$$

E para a complexidade:
$$
O(n^2)
$$

### 4 - Questão
Complexidade de um script dado as complexidades das funções:
1. $fn1() = O(1)$
2. $fn2() = O(1)$
3. $fn3() = O(n^2)$

```py
for i in range(n):
    fn1(i)
    for j in range(n):
        fn2(j)
        for k in range(n):
            fn3(k)
```
- Desenvolvendo a equação geral:
$$
t(n) = \sum_{i=0}^n(1 + \sum_{j=0}^n(1 + \sum_{k=0}^n n²))
$$
$$
=\sum_{i=0}^n1 +\sum_{i=0}^n\sum_{j=0}^n(1+\sum_{k=0}^n n²))
$$
$$
=\sum_{i=0}^n 1 +\sum_{i=0}^n\sum_{j=0}^n 1 + \sum_{i=0}^n\sum_{j=0}^n\sum_{k=0}^n n²
$$
$$
= n + n * n + n * n * n* n²
$$
$$
= n + n² + n^5
$$
A complexidade se da na ordem de $O(n⁴)$


### 5 - Questão
A afirmação é falsa, mesmo que a complexidade do algoritmo B seja menor que a do algoritmo A
um algoritmo apresenta outros fatores que influenciam na sua velocidade total.





