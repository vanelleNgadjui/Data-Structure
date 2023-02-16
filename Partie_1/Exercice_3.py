verite = "Malek le tricheur n’est pas un vrai samouraï"
liste_mots = verite.split()

# Nombre de mots
nb_mots = len(liste_mots)
print(f"Il y a {nb_mots} mots dans la liste")

# Fusionner les mots en string séparés par un espace
nouvelle_verite = " ".join(liste_mots)
print("La nouvelle vérité est :", nouvelle_verite)

# Vérifier si "tricheur" est dans la liste
if "tricheur" in liste_mots:
    print("Le mot 'tricheur' est présent dans la liste")
else:
    print("Le mot 'tricheur' n'est pas présent dans la liste")
