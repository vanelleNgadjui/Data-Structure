# <==================== EXERCICE 4: Carte routière ====================>


import heapq

class Ville:
    def __init__(self, nom):
        self.nom = nom
        self.routes = {}

    def ajouter_route(self, voisin, distance, vitesse_moyenne):
        self.routes[voisin] = (distance, distance/vitesse_moyenne)

class CarteRoutiere:
    def __init__(self):
        self.villes = {}

    def ajouter_ville(self, nom):
        self.villes[nom] = Ville(nom)

    def ajouter_route(self, ville1, ville2, distance, vitesse_moyenne):
        self.villes[ville1].ajouter_route(ville2, distance, vitesse_moyenne)
        self.villes[ville2].ajouter_route(ville1, distance, vitesse_moyenne)

    def trouver_temps_minimum(self, ville_depart, ville_arrivee):
        distances = {ville: float('inf') for ville in self.villes}
        distances[ville_depart] = 0

        heap = [(0, ville_depart)]

        while heap:
            (d, ville_actuelle) = heapq.heappop(heap)

            if ville_actuelle == ville_arrivee:
                return d

            for voisin, route in self.villes[ville_actuelle].routes.items():
                distance = route[0]
                vitesse_moyenne = route[1]
                temps = distance / vitesse_moyenne
                temps_total = d + temps

                if temps_total < distances[voisin]:
                    distances[voisin] = temps_total
                    heapq.heappush(heap, (temps_total, voisin))

        return "Aucun chemin trouvé"

carte = CarteRoutiere()
carte.ajouter_ville("Paris")
carte.ajouter_ville("Lyon")
carte.ajouter_ville("Marseille")

carte.ajouter_route("Paris", "Lyon", 465, 130)
carte.ajouter_route("Lyon", "Marseille", 315, 120)



# Exemple: on prend Paris & Marseille comme villes
print(carte.trouver_temps_minimum("Paris", "Marseille"))