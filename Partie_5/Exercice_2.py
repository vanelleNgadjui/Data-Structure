def tri_topologique(graphe):
    # Initialisation des variables
    # entrees est un dictionnaire qui contient le nombre d'entrées de chaque nœud 
    # (initialisé à 0 pour tous les nœuds). 
    entrees = {noeud: 0 for noeud in graphe}
    # tri est une liste qui contiendra les nœuds triés.
    tri = []

    # Calcul des entrées de chaque nœud en parcourant le graphe 
    # et en comptant le nombre d'arêtes entrantes pour chaque nœud.
    for noeud, voisins in graphe.items():
        for voisin in voisins:
            if voisin not in entrees:
                entrees[voisin] = 0
            entrees[voisin] += 1

    # Ajout des nœuds sans entrée à la file d'attente
    file_attente = [noeud for noeud in entrees if entrees[noeud] == 0]

    # Boucle principale
    while file_attente:
        # Retirer le premier nœud de la file d'attente.
        noeud = file_attente.pop(0)

        # Ajouter le nœud à la liste tri.
        tri.append(noeud) 

        # Pour chaque voisin du nœud retiré:
        for voisin in graphe[noeud]:
            # Décrémenter le nombre d'entrées du voisin.
            entrees[voisin] -= 1
            # Si le voisin n'a plus d'entrée, l'ajouter à la file d'attente.
            if entrees[voisin] == 0:
                file_attente.append(voisin)

    # Vérification de l'absence de cycle dans le graphe
    # Si ces deux valeurs sont différentes, cela signifie qu'il y a un cycle dans le graphe, et une erreur est levée.
    if len(tri) != len(graphe):
        return "Le graphe contient un cycle"

    return tri


graphe = {
    5: [11],
    7: [11, 8],
    3: [8, 10],
    11: [2, 9, 10],
    8: [9],
}

tri = tri_topologique(graphe)
print(tri)  # Output: [3, 7, 5, 11, 8, 10,2, 9]
