# <==================== EXERCICE 3: Binary Trees ====================>



# Partie 1

# 1er arbre binaire
class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droite = None

racine3 = Noeud(5)
racine3.gauche = Noeud(7)
racine3.droite = Noeud(3)
racine3.gauche.gauche = Noeud(4)
racine3.gauche.droite = Noeud(1)
racine3.droite.gauche = Noeud(2)
racine3.droite.droite = Noeud(9)

# 2nd arbre binaire
class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droite = None

racine4 = Noeud(8)
racine4.gauche = Noeud(5)
racine4.droite = Noeud(12)
racine4.gauche.gauche = Noeud(2)
racine4.gauche.droite = Noeud(6)
racine4.droite.gauche = Noeud(10)
racine4.droite.droite = Noeud(15)



# Partie 2

# Fonction qui fusionne les 2 arbres
def fusionner_arbres(arbre1, arbre2):
    # Cas de base : si l'un des arbres est vide, renvoyer l'autre arbre
    if not arbre1:
        return arbre2
    if not arbre2:
        return arbre1

    # Ajouter les valeurs des nœuds correspondants
    arbre1.valeur += arbre2.valeur

    # Fusionner les sous-arbres gauche et droit de chaque nœud
    arbre1.gauche = fusionner_arbres(arbre1.gauche, arbre2.gauche)
    arbre1.droite = fusionner_arbres(arbre1.droite, arbre2.droite)

    return arbre1