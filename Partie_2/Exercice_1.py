# La distance de Hamming est une mesure de similitude entre deux chaînes de même longueur.
# Cette une fonction  renvoie le nombre de positions où les chaînes d'entrée ne correspondent pas.

def distance_hamming(chaine1, chaine2):
    if len(chaine1) != len(chaine2):
        return "Les chaînes n'ont pas la même longueur."
    else:
        distance = 0
        for i in range(len(chaine1)):
            if chaine1[i] != chaine2[i]:
                distance += 1
        return distance

print(distance_hamming("abcd", "abed")) # Renvoie 1
print(distance_hamming("abcde", "abcde")) # Renvoie 0
print(distance_hamming("abc", "def")) # Renvoie 3
print(distance_hamming("abc", "abcd")) # Renvoie "Les chaînes n'ont pas la même longueur."

