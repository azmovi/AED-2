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
=\cancel x_{2} + \cancel x_{3} ... + \cancel x_{n-1} + \cancel x_{n} + x_{n + 1} - x_1 - \cancel x_2  - \cancel x_3  ... - \cancel x_{n -1}- \cancel x_{n}
$$
- Sobrando apenas:
$$
= x_{n+1} - x_1
$$
- Validando a proposta inicial.


### 3 - Questão

