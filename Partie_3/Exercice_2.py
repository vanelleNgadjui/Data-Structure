class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droit = None

def somme_max_noeuds(arbre):
    if arbre is None:
        return 0
    somme_gauche = somme_max_noeuds(arbre.gauche)
    somme_droit = somme_max_noeuds(arbre.droit)
    valeur_max = max(arbre.valeur, arbre.valeur + max(somme_gauche, somme_droit))
    if valeur_max <= 0:
        return 0
    else:
        return valeur_max

# Exemple d'utilisation
noeud1 = Noeud(4)
noeud2 = Noeud(-2)
noeud3 = Noeud(5)
noeud4 = Noeud(8)
noeud5 = Noeud(-3)
noeud6 = Noeud(-1)
noeud7 = Noeud(6)
noeud1.gauche = noeud2
noeud1.droit = noeud3
noeud2.gauche = noeud4
noeud2.droit = noeud5
noeud3.gauche = noeud6
noeud3.droit = noeud7
print(somme_max_noeuds(noeud1)) # Renvoie 15
