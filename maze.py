from turtle import Turtle, Screen
from PIL import Image
import random
import os
cwd = os.getcwd()
imagedir = cwd + "\\data\\images\\"
floormappath = cwd + "\\data\\images\\floormapN17.jpeg"
bi = imagedir + "bi.png"

""" def generate_map_array(filepath):
    img = Image.open(filepath)
    img = img.convert("1") # convert image to black and white
    MAP_ARRAY = list(img.getdata())
    MAP_ARRAY = [MAP_ARRAY[i:i+img.width] for i in range(0, len(MAP_ARRAY), img.width)]
    return MAP_ARRAY

MAP_ARRAY = generate_map_array(bi)
MAP_ARRAY.reverse()  # put 0, 0 in lower left corner
 """

def generate_indoor_map(width, height, obstacle_density, scale):
    MAP_ARRAY = []
    for i in range(height):
        row = []
        for j in range(width):
            if random.random() < obstacle_density:
                row.append('X')
            else:
                row.append('O')
        MAP_ARRAY.append(row)
    
    # Add some elements such as doors and rooms
    for i in range(height):
        for j in range(width):
            if i % scale == 0 and j % scale == 0 and i != 0 and j != 0:
                MAP_ARRAY[i][j] = 'D'  # add a door
                for k in range(i-scale+1, i+scale):
                    for l in range(j-scale+1, j+scale):
                        if 0 <= k < height and 0 <= l < width:
                            MAP_ARRAY[k][l] = 'R'  # add a room
    return MAP_ARRAY

MAP_ARRAY = generate_indoor_map(10, 10, 0.3, 5)

print(MAP_ARRAY)
MAP_ARRAY.reverse()  # put 0, 0 in lower left corner

MAP = '''
XXXXXXXXOX
XOOOOOOOOX
XOXXXXXXXX
XOOOOXXXXX
XXXXOXXXXX
XXXXOXXXXX
XXXXOOOOOX
XXXXXXXXOX
XOOOOOOOOX
XOXXXXXXXX
'''

#MAP_ARRAY = [list(row) for row in MAP.strip().split('\n')]
print(MAP_ARRAY)
#MAP_ARRAY.reverse()  # put 0, 0 in lower left corner

ADJACENT = [
              (0,  1),
    (-1,  0),          (1,  0),
              (0, -1),
]

SCALE = 1

STAMP_SIZE = 20

WIDTH, HEIGHT = len(MAP_ARRAY[0]), len(MAP_ARRAY)

def any_adjacent(x, y):
    return [(x + dx, y + dy) for dx, dy in ADJACENT if 0 <= x + dx < WIDTH and 0 <= y + dy < HEIGHT and MAP_ARRAY[y + dy][x + dx] == 'O']

def movenb():  # slowly navigate the MAP, quit when no where new to go
    x, y = turtle.position()
    adjacent_squares = any_adjacent(int(x), int(y))

    # always moves to first valid adjacent square, need to consider
    # how to deal with forks in the road (e.g. shuffle adjacent_squares)
    for adjacent in adjacent_squares:
        if adjacent not in been_there:
            turtle.goto(adjacent)
            been_there.append(adjacent)
            screen.ontimer(move, 1000)  # one second per move, adjust as needed
            break

def move():
    x, y = turtle.position()
    adjacent_squares = any_adjacent(int(x), int(y))
    random.shuffle(adjacent_squares)
    east_west_adjacent = [(x+dx, y+dy) for dx, dy in ADJACENT if dx == 0] # take only east and west coordinates
    if not adjacent_squares:  # if no valid adjacent squares
        if been_there:  # if turtle has been somewhere before
            turtle.goto(been_there.pop())  # move turtle to previous location
            screen.ontimer(move, 1000)  # continue moving
        else:
            return  # if turtle has not been anywhere before, end the function
    else:
        if len(adjacent_squares) == 2 and (adjacent_squares[0][0] == adjacent_squares[1][0]):
            turtle.goto(east_west_adjacent[0])
            been_there.append(east_west_adjacent[0])
            screen.ontimer(move, 1000)  # continue moving
        else:
            for adjacent in adjacent_squares:
                if adjacent not in been_there:
                    turtle.goto(adjacent)
                    been_there.append(adjacent)
                    screen.ontimer(move, 1000)  # continue moving
                    break
            else:
                turtle.goto(been_there.pop())  # if no new adjacent squares found, move to previous location
                screen.ontimer(move, 1000)  # continue movingdef move():
    x, y = turtle.position()
    adjacent_squares = any_adjacent(int(x), int(y))
    random.shuffle(adjacent_squares)
    east_west_adjacent = [(x+dx, y+dy) for dx, dy in ADJACENT if dx == 0] # take only east and west coordinates
    if not adjacent_squares:  # if no valid adjacent squares
        if been_there:  # if turtle has been somewhere before
            turtle.goto(been_there.pop())  # move turtle to previous location
            screen.ontimer(move, 1000)  # continue moving
        else:
            return  # if turtle has not been anywhere before, end the function
    else:
        if len(adjacent_squares) == 2 and (adjacent_squares[0][0] == adjacent_squares[1][0]):
            turtle.goto(east_west_adjacent[0])
            been_there.append(east_west_adjacent[0])
            screen.ontimer(move, 1000)  # continue moving
        else:
            for adjacent in adjacent_squares:
                if adjacent not in been_there:
                    turtle.goto(adjacent)
                    been_there.append(adjacent)
                    screen.ontimer(move, 1000)  # continue moving
                    break
            else:
                turtle.goto(been_there.pop())  # if no new adjacent squares found, move to previous location
                screen.ontimer(move, 1000)  # continue moving

screen = Screen()  # recast the screen into MAP coordinates
screen.setup(WIDTH * STAMP_SIZE * SCALE, HEIGHT * STAMP_SIZE * SCALE)
screen.setworldcoordinates(-0.5, -0.5, WIDTH - 0.5, HEIGHT - 0.5)

turtle = Turtle('square', visible=False)
turtle.shapesize(SCALE)
turtle.speed('fastest')
turtle.penup()

for y, row in enumerate(MAP_ARRAY):  # draw the MAP
    for x, character in enumerate(row):
        if character == 'X':
            turtle.goto(x, y)
            turtle.stamp()

turtle.color('red')
turtle.shapesize(SCALE / 2)
turtle.goto(1, 0)  # should use unique character in MAP to indicate start & end points
turtle.showturtle()

been_there = []  # prevent doubling back

move()

screen.mainloop()