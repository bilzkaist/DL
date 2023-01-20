import random
import turtle
import networkx as nx

# Create a list of turtles
turtles = [turtle.Turtle() for _ in range(3)]

# Create an empty Graph to store the turtle's locations
G = nx.Graph()

# Define the turtle's movement
def move():
    for t in turtles:
        t.forward(random.randint(1, 5))  # Move the turtle forward by a random distance
        angle = random.randint(0, 360)   # random angle between 0-360
        t.right(angle)                  #  turn turtle by random angle
        x, y = t.position()  # Get the turtle's current position
        G.add_node((x, y))  # Add the turtle's current position to the Graph
        for neighbor in G.nodes():
            if neighbor != (x, y):
                G.add_edge((x, y), neighbor)  # Connect the turtle's current position to its neighbor
        t.stamp()  # Create a copy of the turtle's shape at the current location
        turtle.ontimer(move, 100)  # Repeat the movement every 100 milliseconds

# Start the turtle's movement
move()

# Visualize the turtle's path using the Graph
nx.draw(G, with_labels=True)
turtle.mainloop()
