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
