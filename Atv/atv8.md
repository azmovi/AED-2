# Trabalho 8 - Levada 
    Nome: Antônio Cícero Amorim de Azevedo
    Ra: 811455 
> Fundamentos Básicos de Grafos

### 1 - Questão 
Problema: 9 vértices com 3 arestas por vértices. É possível construir esse grafo?
- A condição de existência de um grafo está baseada no _Handshaking Lema_. Sendo
dada por: a soma dos graus dos vértices de um grafo G é igual a duas vezes o número
de arestas.
$$ \sum_{i=1}^{n} d(v_{i}) = 2m$$

- Substituindo os valores:

$$ 9 * 3  = 2m$$
$$ 27 = 2m$$
$$ m = 13,5$$

- Como podemos perceber o número de arestas deu um valor quebrada, dessa forma
construir o grafo em questão se torna impossível.

### 2 - Questão 
Dado um grafo $G = (V, E)$ provar que $t = (k+1)n - 2m$, sendo $n$ o número de vértices, 
$m$ o número de arestas e deve ter $t$ vértices de grau $k$ e o restante dos 
vértices deve ter grau igual a $k+1$

- Usando o _Handshaking Lema_:
$$\sum_{i=1}^{t} d(v_{i}) \space  + \sum_{i=1}^{n-t} d(v_{i})  = \sum_{i=i}^{n} d(v_{i})$$
$$ t * k \space  + (n-t)*(k+1)  = 2m$$
$$ t * k \space  + n(k+1) - t(k+1)  = 2m$$
$$ t * k \space  + n(k+1) - t*k - t  = 2m$$
$$ n(k+1) - t  = 2m$$
$$t = n(k+1) - 2m$$

### 3 - Questão 
Dado uma festa com $n > 1$ pessoas, existe ao menos duas pessoas com mesmo número
de conhecidos.

- Sabendo que uma pessoa aleatória ela no minimo pode conhecer 0 pessoas, e no máximo
pode conhecer $n-1$ pessoas na festa.

- Analogamente podemos entender que pessoas são vértices de um grafo e que conhecidos
representa o grau desse vértice.

- E supondo que o número de conhecidos cresça de acordo com uma progressão aritmética 
de razão 1:
$$\{0, 1, 2, ..., n-2, n-1\}$$

- Nosso somatório de graus será:
$$ \sum_{i=0}^{n} d(v_{i}) = \frac{(n-1)n}{2} = 2m $$

- Generalizando para um valor de k:
$$\frac{(k-1)k}{2} = 2m$$

- Testando nossa hipóstase para $k+1$, temos que o numero de graus será $2m$ mais
k graus da próxima pessoa:
$$\frac{(k+1-1)(k+1)}{2} = 2m + k$$
$$\frac{(k)(k+1)}{2} = 2m + k$$
$$2m = 2m + k$$
$$0 = k$$
- Chegamos a um absurdo , invalidando nossa hipóstase inicial e validando a proposta
que deve existir ao menos uma pessoa com o mesmo número de conhecidos em uma festa.
