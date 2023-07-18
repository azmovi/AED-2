# Trabalho 6 - Levada 
    Nome: Antônio Cícero Amorim de Azevedo
    Ra: 811455 
> árvore digital de busca (Trie)
### 1 - Questão 
Explicar a busca e inserção de uma Trie, e sua complexidade
###### Busca:
- Supondo que nossa árvore digital é composta apenas de caracteres do alfabeto
ela vai apresentar 5 bits (32 caracteres) e vamos fazendo uma busca binária comparando
zeros e uns presentes no nosso numero binária.
- Dado um bit qualquer na sequencia, se ele for 0 então vamos para a esquerda e
caso ele seja 1 vamos para a direita.
- A cada nível que for descido na árvore nos devemos observar o próximo bit presente
na sequencia.

```py
def busca_trie(tree, char):
    char = char.upper()
    test = tree.root
    bits = bin(ord(char))[4:]
    indice = 0
    while test != None:
        bit = bits[indice]
        if test.key == char:
            return True
        test = test.filho[bit]
    return False
```

