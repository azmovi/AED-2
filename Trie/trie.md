# Trie 
    Professor: Aleandre Levada
    Disciplina: Algortimos e Estrura de Dados
    Grupo:
        Antônio Cícero Amorim de Azevedo (811455)
        João Pedro Mansolelli (811805)
#### Conceito
Posição de um nó depende da comparação entre os bits que compõem as chaves

Transforma uma letra da tabela ASCII em um binário de 5 bits

- Comparando com a Avl Tree:
    - Vantagens: não exige operações de rotações.
    - Desvantagens: desempenho depende do tamanho das chaves.

**Propriedade chave**: A altura está diretamente ligada com o bit da chave que 
está sendo analisado no determinado instante.

#### Busca 
A estratégia proposta consiste em analisar os bits da árvore de acordo com a sua
altura. Começando pela raiz, observamos o bit mais à esquerda e, à medida que 
descemos na árvore, passamos a analisar os bits mais à direita. Isso ajuda a 
explorar a árvore de forma organizada e eficiente, garantindo que todos os níveis 
sejam considerados, o que pode melhorar a tomada de decisões baseadas nos dados 
da árvore.

```py
    def search(self, char:str)->Tuple[Node, int]:
        test = self.root
        if test == None:
            return (None, None)
        binario = bin(ord(char))[4:]
        indice = 0

        while test != None:
            valor = int(binario[indice])
            if test.key == binario:
                break

            else:
                test = test.child[valor]
                indice += 1

        return test, valor

```

#### Inserção 
Nesse processo, o nó será inserido na primeira posição livre de acordo com a ordem
dos bits. Onde dada uma altura K (posição do bit) , os bits das K-1 a cima serão
necessariamente idênticos.

Além do mais, existe apenas nós únicos presentes na árvore, dessa forma não haverá
itens duplicados presentes.

```py
def insert(self, char:str)->bool:
        test = self.root
        binario = bin(ord(char))[4:]
        indice = 0

        while test != None:
            valor = int(binario[indice])
            if test.key == binario:
                print("ja existe esse char na árvore")
                return False

            if test.child[valor] == None:
                novo = Node(char)
                test.child[valor] = novo
                novo.pai = test
                return True

            else:
                test = test.child[valor]
                indice += 1

        if test == None:
            self.root = Node(char)
            return True

        return False 

```
#### Remoção 

Nesse caso devemos nos atentar para que a propriedade das chaves não seja desfeita.

Caso o nó removido seja um no folha, basta tirar a referencia paterna dessa nó que
tudo esta resolvido.

Caso contrario, se o nó que será removido apresentar 1 ou 2 filhos devemos substituir
por um descendente que seja um nó folha, pois continuará atendendo a propriedade 
da chave

```py
    def remove(self, char:str) -> bool:
        node, bit = self.search(char)
        if node != None:
            if node.child[0] == None and node.child[1] == None:
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
