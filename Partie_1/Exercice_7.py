import random
import string
from collections import Counter

def fusion_sets(set1, set2):
    # Fusion des deux sets
    set_unique = set1.union(set2)
    
    # Tri des sets par ordre décroissant
    set1_trie = sorted(set1, reverse=True)
    set2_trie = sorted(set2, reverse=True)
    
    # Somme des valeurs non dupliquées de set1 et set2
    valeurs_non_dupliquees = set_unique - set1.intersection(set2)
    somme_valeurs_non_dupliquees = sum(valeurs_non_dupliquees)
    
    # Création de la chaîne de caractères "lorem ipsum"
    somme_entiers = sum(set1) + sum(set2)
    nb_mots = somme_entiers
    lorem_ipsum = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
    while len(lorem_ipsum.split()) < nb_mots:
        lorem_ipsum += ' ' + ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
    
    # Création du dictionnaire
    dictionnaire = {
        'set_unique': set_unique,
        'set1_trie': set1_trie,
        'set2_trie': set2_trie,
        'somme_valeurs_non_dupliquees': [somme_valeurs_non_dupliquees],
        'lorem_ipsum': lorem_ipsum
    }
    
    return dictionnaire


# Exemple d'utilisation de la fonction
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
resultat = fusion_sets(set1, set2)
print(resultat)
