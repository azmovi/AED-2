from typing import Tuple
from os import system 
from sys import exit
class Node():

    def __init__(self, char:str):
        self.char = char
        self.key = bin(ord(char))[4:]
        self.child = [None, None]
        self.pai = None
        return

class Trie():
    def __init__(self):
        self.root = None 
        return

    def preorder(self, node:Node):
        if self.root == None:
            print("árvore não contem itens")
            return
        if node == None:
            return
        print(node.char, end=" ")
        self.preorder(node.child[0])
        self.preorder(node.child[1])
        return

    def get_pai(self, node:Node)-> Node:
        if node.pai != None:
            return node.pai.char

        return None

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
def menu():

    print("""
[1] Printar a árvore a partir da raiz
[2] Printar a árvore a partir da raiz
[3] Inserção de uma letra
[4] Remoção de uma letra
[5] Sair
""")
    return

def exec(option:int, trie: Trie):
    if option == 1:
        trie.preorder(trie.root)

    elif option == 2:
        char = input('Valor > ')
        while char.isalpha() != True:
            print("Tipo errado, digite novamente")
            char = input('Valor > ')

        valido, _ = trie.search(char)
        if valido != None:
            trie.preorder(char)
        else:
            print("Não existe esse nó na árvore")

    elif option == 3:
        char = input('Valor > ')
        while char.isalpha() != True:
            print("Tipo errado, digite novamente")
            char = input('Valor > ')
        valido = trie.insert(char.upper())
        if valido:
            print("Nó foi inserido")
        else:
            print("Esse nó já está presente na árvore")

    elif option == 4:
        char = input('Valor > ')
        while char.isalpha() != True:
            print("Tipo errado, digite novamente")
            char = input('Valor > ')
        valido = trie.remove(char.upper())
        if valido:
            print("Nó removido com sucesso")
        else:
            print("Esse nó não está presente na árvore")

    elif option == 5:
        print("Até mais...")
        exit(0)

    else:
        print("Opção invalida")
    return

def cls():
    print("")
    input("precione ENTER para voltar o menu")
    system('clear')
    return

def main():
    trie = Trie()
    while True:
        menu()
        option = input("> ")
        while option.isnumeric() == False:
            print("informe um inteiro")
            option = input("> ")

        option = int(option)
        if option not in [1, 2, 3, 4, 5]:
            print("opção inválida")
            continue
        exec(option, trie)
        cls()

    return 

if __name__  == '__main__':
    main()
