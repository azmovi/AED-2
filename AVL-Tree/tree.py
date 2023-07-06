class Avl_tree():

    def __init__(self):
        self.root = None
        return

# Get e setter
    def update_altura(self, no: Node):
        no.altura = 1 + max(self.get_altura(no.left), self.get_altura(no.right))
        return

    def get_altura(self, no: Node) -> int:
        if no == None:
            return 0
        return no.altura

    def get_balance(self, no: Node):
        if no == None:
            return 0
        return self.get_altura(no.left) - self.get_altura(no.right)


# Operações 
    def left_rotate(self, x: Node) -> Node:
        y = x.right
        sub = y.left
        x.right = sub
        self.update_altura(x)
        y.left = x
        self.update_altura(y)

        return y

    def right_rotate(self, y: Node) -> Node:
        x = y.left
        sub = x.right
        y.left = sub
        self.update_altura(y)
        x.right = y
        self.update_altura(x)
        return x

    def left_right_rotate(self, z: Node) -> Node:
        x = z.left
        y = left_rotate(x)
        w = right_rotate(y)
        self.update_altura(z)
        return w

    def right_left_rotate(self, z: Node) -> Node:
        x = z.right
        y = right_rotate(x)
        w = left_rotate(y)
        self.update_altura(z)
        return w

    def fator_balanceamento(self, no):
        if no != None:
            return self.get_altura(no.left) - self.get_altura(no.right)
        return 0

    def balancear(self, no):
        father = no.pai
        if self.fator_balanceamento(father) > 1:
            if self.fator_balanceamento(father.left) >= 0:
                self.right_rotate(father)
            else:
                self.left_right_rotate(father)
            return 
        if self.fator_balanceamento(father) <= -1:
            if self.fator_balanceamento(fator.left) <= 0:
                self.left_rotate(father)
            else:
                self.right_left_rotate(father)
            return
        return

# Inserção de um nó
    def insert_node(self, no: Node):
        x = root
        y = None
        while x != None:
            y = x
            if no.value < x.value:
                x = x.left
            else:
                x = x.right
        no.pai = y
        if y == None:
            root = no
        else:
            if no.value > y.value:
                y.right = no
            else:
                y.left = no

        return 

class Node():
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.pai = None
        self.altura = 1
        return 
