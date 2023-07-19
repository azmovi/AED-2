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
        if node == None:
            return
        print(node.char, self.get_pai(node))
        self.preorder(node.child[0])
        self.preorder(node.child[1])
        return

    def get_pai(self, node:Node)-> Node:
        if node.pai != None:
            return node.pai.char

        return None

    def search(self, char:str)->bool:
        test = self.root
        binario = bin(ord(char))[4:]
        indice = 0

        while test != None:
            valor = int(binario[indice])
            if test.key == binario:
                return True
            else:
                test = test.child[valor]
                indice += 1

        if test == None:
            return False

        return

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

trie = Trie()
trie.insert('a')
trie.insert('b')
trie.insert('z')
trie.insert('c')
trie.insert('n')
trie.preorder(trie.root)
