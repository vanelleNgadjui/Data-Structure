# Opérations sur les listes
# Créez une liste nommée noms qui contient les chaînes de caractères suivantes : "Malek le tricheur", "Nagaakira", "Mitsuakira", "Tsunaakira".

noms = ["Malek le tricheur", "Nagaakira", "Mitsuakira", "Tsunaakira"]
# Écrivez une fonction qui accepte en argument votre liste et une string, et qui ajoute la string spécifiée à la fin de la liste.

def ajouter_nom(liste, nom):
    liste.append(nom)

# Écrivez une autre fonction qui accepte en argument votre liste et une string, et qui supprime la première occurrence de la string spécifiée dans la liste. Si la string n'est pas trouvée dans la liste, la fonction doit renvoyer un message d'erreur approprié.

def supprimer_nom(liste, nom):
    if nom in liste:
        liste.remove(nom)
    else:
        print(f"{nom} n'est pas trouvé dans la liste")



# Exemples d'utilisation
ajouter_nom(noms, "Takeda Shingen")
print(noms)

supprimer_nom(noms, "Nagaakira")
print(noms)

supprimer_nom(noms, "Sanada Yukimura")
