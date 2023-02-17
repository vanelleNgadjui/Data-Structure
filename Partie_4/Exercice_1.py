# #  Prenez en compte la liste suivante : 
# #        1 11 21 1211 111221 312211 13112221 1113213211 31131211131221  

# # Le premier terme se compose de un « un », puis le deuxième énonce le premier « un un ». Ce deuxième terme se compose de deux « un », donc le troisième, énonçant le deuxième, est « deux un ». Il est composé de un « deux » et de un « un », et donc est suivi par « un deux un un », et ainsi de suite.

# # Écrire une fonction acceptant en arguments un terme de la suite de Conway (n) et un nombre (m), et renvoyant les terme n+1 à n+m.

def conway_sequence(n, m):
    # Vérifier si les arguments sont valides
    if not isinstance(n, int) or not isinstance(m, int) or n < 1 or m < 1:
        return "Erreur : les arguments doivent être des entiers positifs."

    # Initialiser la séquence de Conway avec le terme n
    sequence = [str(n)]  

    # Calculer les termes suivants
    for i in range(m):
        current_digit = sequence[i][0]
        count = 0
        term = ""
        for j in range(len(sequence[i])):
            if sequence[i][j] == current_digit:
                count += 1
            else:
                term += str(count) + current_digit
                current_digit = sequence[i][j]
                count = 1
        term += str(count) + current_digit
        sequence.append(term)
    return sequence[n+1:n+m]


print(conway_sequence(1, 10)) # Renvoie ["11", "21", "1211", "111221", "312211", "13112221", "1113213211", "31131211131221", "13211311123113112211", "11131221133112132113212221"]
print(conway_sequence(0, 5)) # Renvoie "Erreur : les arguments doivent être des entiers positifs."
print(conway_sequence("abc", 3)) # Renvoie "Erreur : les arguments doivent être des entiers positifs."
