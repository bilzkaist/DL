import turtle
import random

# Create a screen
screen = turtle.Screen()

# Define the number of particles
num_particles = 1000

# Create a list of particles
particles = [turtle.Turtle() for _ in range(num_particles)]

# Define the initial state of the particles
for particle in particles:
    particle.penup()
    particle.goto(random.randint(-300, 300), random.randint(-300, 300))

# Define the motion model for the particles
def move():
    for particle in particles:
        particle.forward(random.randint(5, 10))
        particle.right(random.randint(-180, 180))
    screen.ontimer(move, 50)  # Repeat the movement every 50 milliseconds

# Start the particle movement
move()

# Show the screen
screen.mainloop()
