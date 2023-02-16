from itertools import product

# La fonction retourne toutes les combinaisons possibles pour obtenir n avec 5 dés à 6 faces.
def combinaisons_des(n):
    if n < 5 or n > 30:
        print("Erreur : n doit être compris entre 5 et 30")
        return None
    else:
        faces = 6
        des = 5
        combinaisons = [x for x in product(range(1, faces+1), repeat=des) if sum(x) == n]
        return combinaisons

# n, représentant un nombre de dés,  5
# m, représentant le nombre de faces des dés (commun à tous les dés), 6
# j le score 
# La fonction doit retourner un dictionnaire comprenant : 
# Plus petit score possible - plus grand score possible - combinaisons possibles pour obtenir j
def scores_possibles(n, m, j):
    if n < 1 or m < 1 or j < n or j > n*m:
        print("Erreur : n, m, j doivent être des entiers positifs, j doit être compris entre n et n*m")
        return None
    else:
        combinaisons = [x for x in product(range(1, m+1), repeat=n) if sum(x) == j]
        score_min = n
        score_max = n*m
        return {"plus petit score possible": score_min,
                "plus grand score possible": score_max,
                "combinaisons possibles": combinaisons}


# Test de la fonction combinaisons_des
combinaisons = combinaisons_des(10)
print(combinaisons)
print(scores_possibles(5,6,10))

