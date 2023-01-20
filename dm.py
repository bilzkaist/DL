import turtle

# Define the hidden map
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

MAP_ARRAY = [list(row) for row in MAP.strip().split('\n')]

# Create a screen
screen = turtle.Screen()

# Set up the turtle
turtle = turtle.Turtle()
turtle.speed("fastest")
turtle.penup()

# Draw the map
for y, row in enumerate(MAP_ARRAY):
    for x, character in enumerate(row):
        turtle.goto(x - (len(row) / 2), -y + (len(MAP_ARRAY) / 2))
        if character == 'X':
            turtle.stamp()

screen.mainloop()
