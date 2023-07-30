# Trabalho 6 - Levada 
    Nome: Antônio Cícero Amorim de Azevedo
    Ra: 811455 
> árvore digital de busca (Trie)
### 1 - Questão 
Explicar a busca e inserção de uma Trie, e sua complexidade
##### Busca:
- Supondo que nossa árvore digital é composta apenas de caracteres do alfabeto
ela vai apresentar 5 bits (32 caracteres) e vamos fazendo uma busca binária comparando
zeros e uns presentes no nosso numero binária.
- Dado um bit qualquer na sequencia, se ele for 0 então vamos para a esquerda e
caso ele seja 1 vamos para a direita.
- A cada nível que for descido na árvore nos devemos observar o próximo bit presente
na sequencia, da esquerda para direita.

```py
def busca_trie(tree, char):
    test = tree.root
    bits = bin(ord(char))[4:]
    indice = 0
    while test != None:
        bit = bits[indice]
        if test.key == char:
            return True
        test = test.filho[bit]
        indice += 1
    return False
```
- Baseado no código apresentado percebemos que se trata de uma busca binária:
$$ t(n) = \sum_{i=0}^{h} (t(\frac{n}{2^i}) + C)$$

- Critério de parada:
$$ 1 = \frac{n}{2^h}$$
$$ 2^h = n$$
$$ \log_{2}{2^h} = \log_{2}{n}$$
$$ h*log_{2}{2} = \log_{2}{n}$$
$$ h = \log_{2}{n}$$

- Voltando para equação principal:

$$ t(n) = \sum_{i=0}^{\log_{2}{n}} (t(\frac{n}{2^i}) + C)$$
$$ t(n) = \sum_{i=0}^{\log_{2}{n}} (t(\frac{n}{2^i}) + C)$$
$$ t(n) = \log_{2}{n} * C$$

- Chegamos que a complexidade da busca é igual:
$$ O(\log_{2}{n})$$

###### Sendo n o numero de bits, que por sua vez representa a altura máxima da árvore. 

##### Inserção:
- Nesse caso bastante parecido com a busca, porém queremos encontrar o local
disponível para a inserção baseado na altura em que ele se encontra.

- Dessa forma se o bit analisado for 0 ele será o filho esquerdo, por outro lado,
se ele for 1 ele será o filho direito.

- Caso a árvore não tenha uma raiz o nó inserido será a raiz.
```py
def insert(self, char:str)->bool:
        test = self.root
        binario = bin(ord(char))[4:]
        indice = 0

        while test != None:
            valor = int(binario[indice])

            if test.child[valor] == None:
                novo = Node(char)
                test.child[valor] = novo
                novo.pai = test
                return True

            test = test.child[valor]
            indice += 1

        if test == None:
            self.root = Node(char)
            return True

        return False 

```
$$ T(n) = 3 + \sum_{i=1}^{h} (T(\frac{n}{2^i}) + C) + 2$$
$$ T(n) = \sum_{i=1}^{\log_{2}n} (T(\frac{n}{2^i}) + C) + C $$
$$ T(n) = \log_{2}{n} * C $$

- Concluímos que a complexidade da inserção será:

$$ O(\log_{2}{n}) $$


### 2 - Questão 
Fazer a inserção dos elementos 
>  D I N S V Y T Q K F A X Z
###### Inserir D:
- valor: 00100
- primeiro valor da árvore logo será a raiz da árvore
###### Inserir I:
- valor: 01001
- bit: 0
- filho esquerdo do nó D
###### Inserir N:
- valor: 01110
- bit: 1
- filho direito do nó I

###### Inserir S:
- valor: 10011
- bit: 1
- filho direito do nó D

###### Inserir V:
- valor: 10110
- bit: 0
- filho esquerdo do nó S

###### Inserir Y:
- valor: 11001
- bit: 1
- filho direito do nó S


###### Inserir T:
- valor: 10100
- bit: 1
- filho direito do nó V

###### Inserir Q:
- valor: 10001
- bit: 0
- filho esquerdo do nó V


###### Inserir K:
- valor: 01011
- bit: 0
- filho esquerdo do nó N

###### Inserir F:
- valor: 00110
- bit: 0
- filho esquerdo do nó I

###### Inserir A:
- valor: 000001
- bit: 0
- filho esquerdo do nó F

###### Inserir X:
- valor: 11000
- bit: 0
- filho esquerdo do nó Y

###### Inserir Z:
- valor: 11010
- bit: 1
- filho direito do nó X

- Concluímos que o formato da árvore quando printamos em pré order sera:
> D I F A N K S V Q T Y X Z



### 3 - Questão 
Explicar o funcionamento da remoção em uma árvore de busca digital a partir do 
seu algoritmo:
```py

def remove(self, char:str) -> bool:
    node, bit = self.search(char)
    if node != None:
        if node.child[0] == None and node.child[1] == None:
            if node.pai == None:
                self.root = None
            else:
                node.pai.child[bit] = None
            return True

        sucessor = node
        while sucessor.child[0] != None or sucessor.child[1] != None:
            if sucessor.child[0] != None:
                sucessor = sucessor.child[0]
                valor = 0
            else:
                sucessor = sucessor.child[1]
                valor = 1

        sucessor.pai.child[valor] = None
        sucessor.pai = node.pai 

        if node.pai != None:
            node.pai.child[bit] = sucessor

        else:
            self.root = sucessor

        if node.child[0] != None:
            sucessor.child[0] = node.child[0]
            node.child[0].pai = sucessor
        if node.child[1] != None:
            sucessor.child[1] = node.child[1]
            node.child[1].pai = sucessor

        return True

    return False
```
- Nesse caso devemos nos atentar para que a propriedade das chaves não seja desfeita.

- Caso o nó removido seja um no folha, basta tirar a referencia paterna dessa nó que
tudo esta resolvido.

- Caso contrario, se o nó que será removido apresentar 1 ou 2 filhos devemos substituir
por um descendente que seja um nó folha, pois continuará atendendo a propriedade 
da chave


### 4 - Questão 
###### Mostrar que a complexidade de busca em uma _Skip List_ é igual a
$O(\log_{d}{n})$:
- A complexidade da _skip list_ está diretamente ligada com o fator de dispersão, 
que é responsável pela probabilidade de um elemento ter um determinado nível, dado
por $\frac{1}{d}$, sendo $d$ um número arbitrário.
