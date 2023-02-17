def decimal_vers_binaire(decimal):
    if type(decimal) != int or decimal < 0:
        return "Erreur : l'entrée n'est pas un nombre entier positif."
    if decimal == 0:
        return '0'
    binaire = ''
    # boucle while : tant que le nombre décimal n'est pas égal à 0, 
    # on calcule le reste de la division par 2 et on l'ajoute à la chaîne de caractères binaire,
    #  puis on divise le nombre décimal par 2 (on utilise l'opérateur // pour effectuer une division entière).
    while decimal > 0:
        binaire = str(decimal % 2) + binaire
        decimal //= 2
    return binaire

# Teste de la fonction
print(decimal_vers_binaire(42)) # '101010'
print( decimal_vers_binaire(10)) # '1010'
print( decimal_vers_binaire(0)) # '0'
print(decimal_vers_binaire(-42)) 
# "Erreur : l'entrée n'est pas un nombre entier positif."
print(decimal_vers_binaire(3.14))
# "Erreur : l'entrée n'est pas un nombre entier positif."
