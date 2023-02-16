

def roman_to_decimal(roman_numeral): 
    roman_to_decimal_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    decimal_value = 0
    previous_value = 0

    for numeral in roman_numeral:
        current_value = roman_to_decimal_map[numeral]
        if current_value > previous_value:
            decimal_value += current_value - 2 * previous_value 
        else:
            decimal_value += current_value
        previous_value = current_value

    return decimal_value 

print(roman_to_decimal('XV'))


def decimal_to_roman(decimal_num):
    decimal_to_roman_map = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    roman_numeral = ''
    for decimal_value, roman_value in decimal_to_roman_map.items():
        while decimal_num >= decimal_value:
            roman_numeral += roman_value
            decimal_num -= decimal_value

    return roman_numeral

print(decimal_to_roman(125))  

print(decimal_to_roman(3999))
