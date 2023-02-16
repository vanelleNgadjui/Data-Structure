# 1. Création de la liste "noms"
noms = ["Malek le tricheur", "Nagaakira", "Mitsuakira", "Tsunaakira", "Tsunanaga"]

# 2. Définition de la fonction "get_nom"
def get_nom(liste, index):
    if index < 0 or index >= len(liste):
        return "L'index spécifié est en dehors des limites de la liste."
    else:
        return liste[index]

# Utilisation de la fonction "get_nom" avec différents index
print(get_nom(noms, 0))  # Affiche "Malek le tricheur"
print(get_nom(noms, 2))  # Affiche "Mitsuakira"
print(get_nom(noms, 4))  # Affiche "Tsunanaga"
print(get_nom(noms, -1))  # Affiche "L'index spécifié est en dehors des limites de la liste."
print(get_nom(noms, 5))  # Affiche "L'index spécifié est en dehors des limites de la liste."
