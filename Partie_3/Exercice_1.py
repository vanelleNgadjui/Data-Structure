# # Fonction qui prend en entrée 3 valeurs RGB (R, G et B) et renvoie leur représentation hexadécimale correspondante. 
# #  la fonction convertit chaque valeur RGB en hexadécimal en utilisant la fonction "hex()"
def rgb_to_hex(r, g, b):
    # Vérifier si les valeurs RGB sont valides
    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        return "Erreur : les valeurs RGB doivent être comprises entre 0 et 255."

    # Convertir les valeurs RGB en hexadécimal
    hex_r = hex(r)[2:].zfill(2)
    hex_g = hex(g)[2:].zfill(2)
    hex_b = hex(b)[2:].zfill(2)

    # Concaténer les valeurs hexadécimales
    hex_code = hex_r + hex_g + hex_b

    return hex_code.upper()

print(rgb_to_hex(255, 0, 0)) # Renvoie "FF0000"
print(rgb_to_hex(0, 128, 64)) # Renvoie "008040"
print(rgb_to_hex(300, 128, 64)) # Renvoie "Erreur : les valeurs RGB doivent être comprises entre 0 et 255."
print(rgb_to_hex(255, 255, 255)) # Renvoie "FFFFFF"

