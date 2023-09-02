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
        self.matrix[c][l] = size

        return 

    def show(self):
        for linha in range(self.vertices):
            print(self.matrix[linha])
        return

def dijkstra(grafo: Grafo, inicio:int):
    distancias = {}
    predecessor = {}
    visitados = set()
    for vertice in range(grafo.vertices):
        distancias[vertice] = float("inf")
        predecessor[vertice] = None
    distancias[inicio] = 0
    pqueue = []
    heapq.heappush(pqueue, (0, inicio))

    while len(pqueue) != 0:
        d_atual, v_atual = heapq.heappop(pqueue)
        visitados.add(v_atual)

        for vizinho in range(grafo.vertices):
            if grafo.matrix[v_atual][vizinho] != 0 and vizinho not in visitados:
                distancia = grafo.matrix[v_atual][vizinho]
                # Relax
                if d_atual + distancia < distancias[vizinho]:
                    distancias[vizinho] = d_atual + distancia
                    heapq.heappush(pqueue, (distancias[vizinho], vizinho))

                    predecessor[vizinho] = v_atual

    return distancias, predecessor



test = Grafo(5)
test.add_arestas(0, 4, 20)
test.add_arestas(0, 1, 10)
test.add_arestas(1, 4, 50)
test.add_arestas(3, 4, 70)
test.add_arestas(1, 3, 40)
test.add_arestas(2, 3, 60)
test.add_arestas(1, 2, 30)
test.show()
distancias, predecessor = (dijkstra(test, 0))

print("distancias = ", distancias)
print("predecessor = ", predecessor)

