import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, city1, city2, distance, speed):
        self.graph[city1][city2] = {'distance': distance, 'speed': speed}
        self.graph[city2][city1] = {'distance': distance, 'speed': speed}

    def shortest_time(self, start, end):
        # Initialisation des distances et des nœuds visités
        distances = {city: float('inf') for city in self.graph}
        distances[start] = 0
        visited = set()

        # Initialisation de la file de priorité avec le nœud de départ
        heap = [(0, start)]

        while heap:
            # Extraction du nœud avec la plus petite distance
            (dist, current) = heapq.heappop(heap)

            # Si on a atteint la ville d'arrivée, on peut arrêter
            if current == end:
                return distances[end]

            # Si on a déjà visité ce nœud, on passe au suivant
            if current in visited:
                continue

            visited.add(current)

            # Mise à jour des distances pour les nœuds adjacents non visités
            for neighbor, data in self.graph[current].items():
                if neighbor in visited:
                    continue

                distance = data['distance']
                speed = data['speed']
                time = distance / speed

                new_distance = distances[current] + time
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(heap, (new_distance, neighbor))

        # Si on n'a pas atteint la ville d'arrivée, il n'y a pas de chemin
        raise ValueError("Pas de chemin entre les deux villes")

# Exemple d'utilisation
g = Graph()

g.add_edge('Paris', 'Lyon', 465, 130)
g.add_edge('Lyon', 'Marseille', 315, 110)
g.add_edge('Paris', 'Bordeaux', 583, 130)
g.add_edge('Bordeaux', 'Toulouse', 245, 120)
g.add_edge('Toulouse', 'Marseille', 403, 110)

start = 'Paris'
end = 'Marseille'

try:
    shortest_time = g.shortest_time(start, end)
    print(f"Le temps minimum pour se déplacer de {start} à {end} est de {shortest_time:.2f} heures.")
except ValueError as e:
    print(e)
