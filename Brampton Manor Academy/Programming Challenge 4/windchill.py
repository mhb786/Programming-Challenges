def calculation (air_temp, air_speed):
    return 35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16

values = [[10,15], [0,25], [-10,35]]

for value in values:
    print(f'Temperature of {value[0]} and speed of {value[1]} gives windchill of: {calculation(value[0], value[1])}')

air_temp = float(input('Temperature: '))
air_speed = float(input('Speed: '))

print(f'Windchill: {calculation(air_temp, air_speed)}')