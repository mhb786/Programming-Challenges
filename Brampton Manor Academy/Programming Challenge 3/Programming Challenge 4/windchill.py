def calculation (air_temp, air_speed):
    return 35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16

air_temp = float(10)
air_speed = float(15)

print(f'Temperature of {air_temp} and speed of {air_speed} gives windchill of: {calculation(air_temp, air_speed)}')

air_temp = float(0)
air_speed = float(25)

print(f'Temperature of {air_temp} and speed of {air_speed} gives windchill of: {calculation(air_temp, air_speed)}')

air_temp = float(-10)
air_speed = float(35)

print(f'Temperature of {air_temp} and speed of {air_speed} gives windchill of: {calculation(air_temp, air_speed)}')

air_temp = float(input('Temperature: '))
air_speed = float(input('Speed: '))

print(f'Windchill: {calculation(air_temp, air_speed)}')