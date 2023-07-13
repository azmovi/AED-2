class Node():
    def __init__(self, value: int):
        self.value = value
        self.right = None
        self.left = None
        self.pai = None
        self.altura = 1 
        return


class Avl():
    def __init__(self):
        self.root = None

    def preorder(self, no: Node = None):
        if no == None:
            return 
        print(no.value, self.fator_balanceamento(no), self.get_pai(no))
        self.preorder(no.left)
        self.preorder(no.right)
        return

    def get_value(self, no:Node):
        if no == None:
            return None
        return no.value

    def get_pai(self, no:Node):
        if no.pai == None:
            return None

        return no.pai.value

    def insert(self, valor:int):
        no = Node(valor)
        x = self.root
        y = None
        while x != None:
            y = x
            if no.value > x.value:
                x = x.right
            else:
                x = x.left
        if y == None:
            self.root = no
        else:
            no.pai = y
            if no.value > y.value:
                y.right = no
            else:
                y.left = no

        self.tree_altura_update(no)


        novo_no = no
        self.rebalanceamento_insert(no, novo_no)

        return

    def rebalanceamento_insert(self, no:Node, novo_no:Node):
        while no != None:
            self.update_altura(no)
            fb = self.fator_balanceamento(no)
            if fb not in [-1, 0, 1]:
                self.rotation_insert(no, novo_no, fb)
            no = no.pai
        return

    def rotation_insert(self, no:Node, novo_no:Node, fb:int):
        if fb > 1:
            if novo_no.value <= no.left.value:
                self.right_rotate(no)
                return 
            else:
                #rotaçao esquerda direita
                xpto = no.left
                self.left_rotate(xpto)
                self.right_rotate(no)
                return 
        if fb < -1:
            if novo_no.value > no.right.value:
                self.left_rotate(no)
                return
            else:
                xpto = no.right
                self.right_rotate(xpto)
                self.left_rotate(no)
                return
        return

    def update_altura(self, no: Node) -> Node:
        if no == None:
            return 0
        altura_left = self.update_altura(no.left)
        altura_right = self.update_altura(no.right)
        no.altura = 1 + max(altura_left, altura_right)
        return no.altura

    def tree_altura_update(self, no: Node):
        while no != None:
            self.update_altura(no)
            no = no.pai
        return 

    def fator_balanceamento(self, no: Node) -> int:
        if no == None:
            return 0
        altura_left = self.get_altura(no.left)
        altura_right = self.get_altura(no.right)
        return altura_left - altura_right

    def get_altura(self, no: Node) -> int:
        if no == None:
            return 0
        return no.altura

    def left_rotate(self, x: Node):
        y = x.right
        if y == None:
            return
        sub = y.left

        y.left = x
        x.right = sub

        if sub != None:
            sub.pai = x

        y.pai = x.pai
        if x.pai == None:
            self.root = y
        elif x == x.pai.left:
            x.pai.left = y
        else:
            x.pai.right = y

        x.pai = y

        self.update_altura(y)
        self.update_altura(x)

        return

    def right_rotate(self, y: Node):
        x = y.left
        if x == None:
            return
        sub = x.right  

        x.right = y
        y.left = sub
        if sub != None:
            sub.pai = x

        x.pai = y.pai
        if y.pai == None:
            self.root = x
        elif y == y.pai.left:
            y.pai.left = x
        else:
            y.pai.right = x

        y.pai = x
        self.update_altura(y)
        self.update_altura(x)

        return

    def find(self, valor: int) -> bool:
        no = Node(valor)
        test = self.root
        while test:
            if no.value > test.value:
                test = test.right
            elif no.value < test.value:
                test = test.left
            else:
                return test
        return None

    def remove(self, valor: int):
        no = self.find(valor)

        if no:
            folha = False
            raiz = False
            esquerda = False
            direita = False

            if no.pai == None:
                raiz = True
                self.root = None
            elif no.pai.left == no:
                esquerda = True
                no.pai.left = None
            else:
                direita = True
                no.pai.right = None

            if no.left == None and no.right == None:
                folha = True

            if folha:
                self.rebalanceamento_delete(no.pai)
                return True  # Retorne True para indicar que a remoção foi bem-sucedida
        return False  # Retorne False se o nó não for encontrado



    def rebalanceamento_delete(self, no: Node):
        while no != None:
            self.update_altura(no)
            fb = self.fator_balanceamento(no)

            fb_esquerdo = 0
            if no.left != None:
                fb_esquerdo = self.fator_balanceamento(no.left)

            if fb > 1:
                if fb_esquerdo >= 0:
                    self.right_rotate(no)
                else:
                    xpto = self.left_rotate(no)
                    self.right_rotate(xpto)
            if fb <= -1:
                if fb_esquerdo <= 0:
                    self.left_rotate(no)
                else:
                    xpto = self.right_rotate(no)
                    self.left_rotate(xpto)

            no = no.pai
        return


arvore = Avl()
arvore.insert(33)
arvore.insert(13)
arvore.insert(11)
arvore.insert(21)
arvore.insert(53)
arvore.insert(61)
arvore.insert(8)
arvore.insert(9)
print(arvore.remove(61))
arvore.preorder(arvore.root)
