def tri_par_insertion(liste):
    if type(liste) != list or len(liste) != 30:
        return "Erreur : l'entrée n'est pas une liste de 30 entiers."
    for i in range(1, len(liste)):
        cle = liste[i]
        j = i - 1
        while j >= 0 and liste[j] > cle:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = cle
    return liste


print(tri_par_insertion([5, 3, 8, 9, 1, 7, 0, 2, 6, 4]))
# "Erreur : l'entrée n'est pas une liste de 30 entiers."
print(tri_par_insertion([5, 3, 8, 9, 1, 7, 0, 2, 6, 4]*3))
# [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]
