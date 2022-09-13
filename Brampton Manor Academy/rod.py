rods = float(input('Input rods: '))
print(f'You input {rods} rods. \n \nConversions')


def meters(rods):
    return rods * 5.0292

meters = meters(rods)
print(f'Meters: {meters}')


def feet(meters):
    return float(meters / 0.3048)

feet = feet(meters)
print(f'Feet: {feet}')


def miles(meters):
    return meters / 1609.34

miles = miles(meters)
print(f'Mile: {miles}')


def furlong(rods):
    return rods / 40

furlong = furlong(rods)
print(f'Furlong: {furlong}')


def walking_speed(miles):
    return (miles * 60) / 3.1

walking_speed = walking_speed(miles)
print(f'Minutes to walk {rods} rods: {walking_speed}')
