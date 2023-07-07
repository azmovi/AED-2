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
        print(no.value, self.fator_balanceamento(no))
        self.preorder(no.left)
        self.preorder(no.right)
        return

    def insert(self, no:Node):
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

        """while no != None:
            fb = self.fator_balanceamento(no)
            if fb not in [1, 0, -1]:
                self.rotation(no, fb, novo_no)
            no = no.pai"""


        return

    def rotation(self, no:Node, fb: int, novo_no:Node):
        if fb > 1:
            if no.left != None and novo_no.value <= no.left.value:
                self.right_rotate(no)
            else:
                self.left_right_rotate(no)
            return
        if fb < -1:
            if no.right != None and novo_no.value > no.right.value:
                self.left_rotate(no)
            else:
                self.right_left_rotate(no)
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
        sub = y.left
        x.right = sub 
        y.left = x

        self.tree_altura_update(y)
        self.tree_altura_update(x)

        y.pai = x.pai
        x.pai = y

        if sub != None:
            sub.pai = x

        return y

    def right_rotate(self, y: Node):
        x = y.left
        sub = x.right
        y.left = sub
        x.right = y

        self.tree_altura_update(x)
        self.tree_altura_update(y)

        x.pai = y.pai
        y.pai = x

        if sub != None:
            sub.pai = y

        return x

    def left_right_rotate(self, z: Node):
        x = z.left
        y = self.left_rotate(x)
        w = self.right_rotate(y)

        self.tree_altura_update(z)
        return w

    def right_left_rotate(self, z: Node):
        x = z.right
        y = self.right_rotate(x)
        w = self.left_rotate(y)

        self.tree_altura_update(z)
        return w




arvore = Avl()
arvore.insert(Node(33))
arvore.insert(Node(13))
arvore.insert(Node(53))
arvore.insert(Node(61))
arvore.insert(Node(21))
arvore.insert(Node(11))
no8 = Node(8)
arvore.insert(no8)
arvore.insert(Node(9))
#arvore.left_rotate(no8)
arvore.preorder(arvore.root)
