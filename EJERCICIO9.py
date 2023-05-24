import random

class Grafo:
    def __init__(self, num_planetas):
        self.grafo = [[0 for _ in range(num_planetas)] for _ in range(num_planetas)]
        self.planetas = []
    
    def agregar_planeta(self, nombre):
        self.planetas.append(nombre)
    
    def agregar_arista(self, planeta1, planeta2, peso):
        i1 = self.planetas.index(planeta1)
        i2 = self.planetas.index(planeta2)
        self.grafo[i1][i2] = peso
        self.grafo[i2][i1] = peso


def prim(graph):
    num_nodes = len(graph.grafo)
    visited = [False] * num_nodes
    weights = [float('inf')] * num_nodes
    weights[0] = 0
    parents = [-1] * num_nodes

    for _ in range(num_nodes):
        min_weight = float('inf')
        node = -1
        for i in range(num_nodes):
            if not visited[i] and weights[i] < min_weight:
                min_weight = weights[i]
                node = i
        visited[node] = True
        for i in range(num_nodes):
            if graph.grafo[node][i] > 0 and not visited[i]:
                if weights[i] > graph.grafo[node][i]:
                    weights[i] = graph.grafo[node][i]
                    parents[i] = node

    mst = []
    for i in range(1, num_nodes):
        mst.append((graph.planetas[parents[i]], graph.planetas[i], weights[i]))
    return mst


def dijkstra(graph, origen):
    num_nodes = len(graph.grafo)
    visited = [False] * num_nodes
    distances = [float('inf')] * num_nodes
    previous = [-1] * num_nodes
    origen_index = graph.planetas.index(origen)
    distances[origen_index] = 0

    for _ in range(num_nodes):
        min_distance = float('inf')
        node = -1
        for i in range(num_nodes):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                node = i
        visited[node] = True
        for i in range(num_nodes):
            if graph.grafo[node][i] > 0 and not visited[i]:
                new_distance = distances[node] + graph.grafo[node][i]
                if new_distance < distances[i]:
                    distances[i] = new_distance
                    previous[i] = node

    return distances, previous

def shortest_path(graph, origen, destino):
    distances, previous = dijkstra(graph, origen)
    path = []
    current_node = graph.planetas.index(destino)
    while current_node != -1:
        path.append(graph.planetas[current_node])
        current_node = previous[current_node]
    path.reverse()
    return path


def dfs(graph, start):
    stack = [start]
    visited = {start}

    while stack:
        planet = stack.pop()
        for i, connection in enumerate(graph.grafo[graph.planetas.index(planet)]):
            if connection != 0 and graph.planetas[i] not in visited:
                stack.append(graph.planetas[i])
                visited.add(graph.planetas[i])
    return visited


planetas = ["Alderaan", "Endor", "Dagobah", "Hoth", "Tatooine", "Kamino", "Naboo", "Mustafar", "Scarif", "Bespin", 
            "Jakku", "Kashyyyk", "Coruscant", "Yavin 4", "Lothal", "Geonosis", "Kessel"]

num_planetas = len(planetas)
grafo = Grafo(num_planetas)

for planeta in planetas:
    grafo.agregar_planeta(planeta)

for planeta in grafo.planetas:
    otros_planetas = grafo.planetas.copy()
    otros_planetas.remove(planeta)
    conexiones = random.sample(otros_planetas, 4)
    for conexion in conexiones:
        grafo.agregar_arista(planeta, conexion, random.randint(1, 100))


arbol_expansion_minima_prim = prim(grafo)

print("Árbol de expansión mínima:")
print(arbol_expansion_minima_prim)
print("\n")

camino_tatooine_dagobah = shortest_path(grafo, 'Tatooine', 'Dagobah')
camino_alderaan_endor = shortest_path(grafo, 'Alderaan', 'Endor')
camino_hoth_tatooine = shortest_path(grafo, 'Hoth', 'Tatooine')

print('Camino más corto de Tatooine a Dagobah: ', camino_tatooine_dagobah)
print('Camino más corto de Alderaan a Endor: ', camino_alderaan_endor)
print('Camino más corto de Hoth a Tatooine: ', camino_hoth_tatooine)
print("\n")

visited_planets = dfs(grafo, 'Tatooine')
print('Planetas accesibles desde Tatooine: ', visited_planets)
