# <==================== EXERCICE 2: 7 segments ====================>

def decimal_to_7segment(decimal_number):
    segments = {
        '0': ('###', '# #', '# #', '# #', '###'),
        '1': ('  #', '  #', '  #', '  #', '  #'),
        '2': ('###', '  #', '###', '#  ', '###'),
        '3': ('###', '  #', '###', '  #', '###'),
        '4': ('# #', '# #', '###', '  #', '  #'),
        '5': ('###', '#  ', '###', '  #', '###'),
        '6': ('###', '#  ', '###', '# #', '###'),
        '7': ('###', '  #', '  #', '  #', '  #'),
        '8': ('###', '# #', '###', '# #', '###'),
        '9': ('###', '# #', '###', '  #', '###'),
        '.': ('   ', '   ', '   ', '   ', ' # '),
        '-': ('   ', '   ', '###', '   ', '   '),
        ' ': ('   ', '   ', '   ', '   ', '   ')
    }

    digits = [segments[d] for d in str(decimal_number)]

    # Concaténer les segments horizontalement
    rows = []
    for i in range(5):
        row = ''
        for digit in digits:
            row += digit[i] + ' '
        rows.append(row)

    # Concaténer les rangées verticalement
    return '\n'.join(rows)


# Exemple d'utilisation avec '30'
print(decimal_to_7segment(30))
