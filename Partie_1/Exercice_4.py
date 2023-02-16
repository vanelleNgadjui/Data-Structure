# Créer le dictionnaire
dic = {"Nagaakira": 25, "Mitsuakira": 33, "Tsunaakira": 39}

# Fonction pour vérifier si une clé est présente dans un dictionnaire
def verif_cle(dic, cle):
    return cle in dic

# Fonction pour ajouter une entrée au dictionnaire
def ajouter_entree(dic, cle, valeur):
    dic[cle] = valeur

# Exemples d'utilisation
if verif_cle(dic, "Nagaakira"):
    print("La clé 'Nagaakira' est présente dans le dictionnaire")
else:
    print("La clé 'Nagaakira' n'est pas présente dans le dictionnaire")

ajouter_entree(dic, "Kenshin", 28)
print(dic)
