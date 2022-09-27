import turtle
import math

starting_x = 0
starting_y = 0
one_x = int(input('Enter the x coordinate for the first point: '))
one_y = int(input('Enter the y coordinate for the first point: '))
two_x = int(input('Enter the x coordinate for the second point: '))
two_y = int(input('Enter the y coordinate for the second point: '))

turtle.fillcolor('green')
turtle.title("Turtle Angle Calculator")
turtle.write('I will calculate the angle between these two lines')

turtle.goto(one_x, one_y)
turtle.goto(two_x, two_y)

def calculate_gradient(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def calculate_angle(m2, m1):
    tan_angle = abs((m2 - m1)) / (1 + m1*m2)
    angle = math.atan(tan_angle)
    angle *= 180 / math.pi
    return angle

gradient1 = calculate_gradient(starting_x, starting_y, one_x, one_y)
gradient2 = calculate_gradient(one_x, one_y, two_x, two_y)

turtle.write(f'The angle between the two lines is {abs(calculate_angle(gradient2, gradient1))}')
turtle.done()
