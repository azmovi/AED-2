import heapq

class Grafo():
    def __init__(self, vertices:int):
        self.vertices = vertices
        self.matrix = [[0 for coluna in range(vertices)]for linha in range(vertices)]

        return

    def add_arestas(self, l, c, size):
        if l == c:
            print("Não existe arestas no mesmo vertice")

        self.matrix[l][c] = size 
        return 

    def show(self):
        for linha in range(self.vertices):
            print(self.matrix[linha])
        return

def bellman_ford(grafo: Grafo, inicio:int):
    distancias = {}
    predecessor = {}
    visitados = set()
    for vertice in range(grafo.vertices):
        distancias[vertice] = float("inf")
        predecessor[vertice] = None
        
    distancias[inicio] = 0
    for _ in range(grafo.vertices - 1):
        for origem in range(grafo.vertices):
            for destino in range(grafo.vertices):
                if origem != destino and grafo.matrix[origem][destino] != 0:
                    distancia_atual = grafo.matrix[origem][destino]
                    if distancias[origem] + distancia_atual < distancias[destino]:
                        distancias[destino] = distancias[origem] + distancia_atual
                        predecessor[destino] = origem
    return distancias, predecessor



test = Grafo(5)
test.add_arestas(0, 1, 6)
test.add_arestas(0, 3, 7)
test.add_arestas(4, 0, 2)
test.add_arestas(1, 2, 5)
test.add_arestas(1, 4, -4)
test.add_arestas(1, 3, 8)
test.add_arestas(2, 1, -2)
test.add_arestas(3, 2, -3)
test.add_arestas(4, 2, 7)
test.add_arestas(3, 4, 9)
test.show()
distancias, predecessor = bellman_ford(test, 0)
print("distancias = ", distancias)
print("predecessor = ", predecessor)

