# Trabalho 5 - Levada 
    Nome: Antônio Cícero Amorim de Azevedo
    Ra: 811455 
> Árvore AVL
### 1 - Questão 
- As árvores AVL são auto balanceadas, dessa forma quando ocorre uma remoção ou
uma inserção, ocorre um rebalanceamento dos nós para que todos fiquem uniformes
dentro da árvore, dessa forma a árvore nunca irá pender para os lados um problema 
bastante comum na árvore binária normal, que quando muito desbalanceada perde a 
propriedade de busca na complexidade $O(\log{n})$

### 2 - Questão
- Sobre árvores AVL:
###### A) Explicar rotação a esquerda:

- Quando um nó (x) tem o fator de balanceamento menor que $-1$, temos que o ramo da
direita é maior que o da esquerda. Dessa forma para balancear devemos verificar
se o filho direito de x(y) tem um parente esquerdo, se tiver devemos fazer a
troca de referencia, onde quem vai passar a ser o filho direito de x será o filho
esquerdo de y. Próxima etapa é verificar se x é filho de alguém, se for saber se
ele é filho direito ou esquerdo e apontar esse parentesco para o y no lugar de x,
se não y vai passar a ser raiz dessa árvore. Por ultimo devemos colocar x como 
filho esquerdo de y. Dessa forma a rotação a esquerda está completa.


###### B) Explicar rotação a direita:

- Quando um nó (y) tem o fator de balanceamento maior $1$, temos que o ramo da esquerda
está maior que o ramo da direita. Dessa forma para balancear devemos verificar se
o filho da esquerda (x) de y tem um parente direito, se tiver devemos fazer com
que o filho esquerdo de y seja o filho direito de x. O próximo passo é encontrar 
o pai de y, se ele tiver devemos saber se y é um filho esquerdo ou direito e dar
essa referencia para x, caso não tenha x vai passar a ser a raiz dessa árvore.
Por ultimo devemos fazer que agora o filho direito de x seja agora y. Finalizando
o processo de rotação.


### 3 - Questão
Explicar a rotação direita esquerda:
- Ela é aplicada quando um nó (z) possui uma sub árvore direita maior que a sub
árvore esquerda, ou seja, quando o fator de balanceamento for menor $-1$ e o filho
da direita (x) possuir uma sub árvore esquerda maior que a sub árvore da direita,
ou seja, o fator de balanceamento maior que $1$.
- Como o nome diz devemos fazer uma rotação direita em x e após isso deve ser feito
uma rotação esquerda em z, que terá suas sub árvores já modificadas pela rotação
anterior.


### 4 - Questão
Explicar a rotação esquerda direita:
- Ela é aplicada quando um nó (z) possui uma sub árvore esquerda maior que a sub
árvore direita, ou seja, quando o fator de balanceamento for maior que $1$ e o 
filho esquerdo (x) de z possuir uma sub árvore direita maior que a sub árvore esquerda,
ou seja, o fator de balanceamento é menor que $-1$.
- Deve forma devemos fazer a rotação esquerda no nó x e depois com o nó z devemos
fazer a rotação direita com a nova formação das sub árvores para que fique 
equilibrado.

### 5 - Questão
Inserção do elemento 39 em uma árvore AVL e a remoção do elemento 25.

```
21
├── 15
│   ├── 12
│   │   ├── 10
│   │   │   ├── 7
│   │   │   └── 11
│   │   └── 13
│   └── 18
│       ├── 17
│       │   └── 16
│       └── 19
│           └── 20
└── 25
    ├── 23
    │   ├── 22
    │   └── 24
    └── 30
        ├── 29
        └── 35
            ├── 33
            └── 40
```
##### Inserção:
- Nesse caso devemos inserir o $39$ como filho direito do nó 35, por sua vez terá
como filho direito sendo o nó $40$.
```
21
├── 15
│   ├── 12
│   │   ├── 10
│   │   │   ├── 7
│   │   │   └── 11
│   │   └── 13
│   └── 18
│       ├── 17
│       │   └── 16
│       └── 19
│           └── 20
└── 25
    ├── 23
    │   ├── 22
    │   └── 24
    └── 30
        ├── 29
        └── 35
            ├── 33
            └── 39
                └── 40
```

- Com isso o nó $30$ se encontra com o fator de balanceamento $-2$ e deve ser 
feito uma rotação para a esquerda:
```
21
├── 15
│   ├── 12
│   │   ├── 10
│   │   │   ├── 7
│   │   │   └── 11
│   │   └── 13
│   └── 18
│       ├── 17
│       │   └── 16
│       └── 19
│           └── 20
└── 25
    ├── 23
    │   ├── 22
    │   └── 24
    └── 35
        ├── 30
        │   ├── 29
        │   └── 33
        └── 39
            └── 40
```
###### Etapas
- Filho direito do nó $25$ vai apontar para o nó $35$
- Filho esquerdo do no $35$ vai apontar para o filho direito do nó $30$
- O pai do nó $30$ passa a ser o nó $35$

###### Remoção
- Próxima etapa é remover o elemento $25$ da árvore e fazer o balanceamento dela
- Após a remoção devemos achar o sucessor do nó $25$, já que ele não é uma folha
- Nesse caso o sucessor é o nó $29$, onde deve-se retirar o o parentesco com o
nó $30$ e dar para o nó $21$
```
21
├── 15
│   ├── 12
│   │   ├── 10
│   │   │   ├── 7
│   │   │   └── 11
│   │   └── 13
│   └── 18
│       ├── 17
│       │   └── 16
│       └── 19
│           └── 20
└── 29
    ├── 23
    │   ├── 22
    │   └── 24
    └── 35
        ├── 30
        │   └── 33
        └── 39
            └── 40
```
