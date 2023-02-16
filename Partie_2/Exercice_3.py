def phone_number(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10):
    phone_number = '({}{}{}) {}{}{}-{}{}{}{}'.format(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10)
    return phone_number

print(phone_number(2, 1, 2, 5, 5, 5, 1, 2, 3, 4))


def format_phone_number(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10):
    phone_number = '{}{}{}{}{}{}{}{}{}{}'.format(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10)
    return {
        'États-Unis': '+1 {}'.format(phone_number[0:3]) + ' ' + phone_number[3:6] + '-' + phone_number[6:],
        'France': '+33 {}'.format(phone_number[1:3]) + ' ' + phone_number[3:5] + ' ' + phone_number[5:7] + ' ' + phone_number[7:9] + ' ' + phone_number[9:],
        'Japon': '+81 {}'.format(phone_number[0:3]) + '-' + phone_number[3:7] + '-' + phone_number[7:]
    }

print(format_phone_number(2, 1, 2, 5, 5, 5, 1, 2, 3, 4))