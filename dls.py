import random
import matplotlib.pyplot as plt
import imageio
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D
import numpy as np

# Sample data for employee positions and movements
positions = {
    "Alice": [(random.uniform(1,12), random.uniform(1,12)) for _ in range(5)],
    "Bob": [(random.uniform(1,12), random.uniform(1,12)) for _ in range(5)],
    "Charlie": [(random.uniform(1,12), random.uniform(1,12)) for _ in range(5)],
    "David": [(random.uniform(1,12), random.uniform(1,12)) for _ in range(5)],
    "Eve": [(random.uniform(1,12), random.uniform(1,12)) for _ in range(5)]
}

# Create a figure and axis
fig, ax = plt.subplots()

# Plot employee positions
scat = ax.scatter([], [])

# Add double head arrow connecting employees
lines = [Line2D([], [], color='black', lw=1.5) for _ in range(len(positions)*(len(positions)-1)//2)]

for line in lines:
    ax.add_line(line)


def update(num):
    x_pos = [p[0] for employee in positions.keys() for p in positions[employee][:num+1]]
    y_pos = [p[1] for employee in positions.keys() for p in positions[employee][:num+1]]
    scat.set_offsets(np.c_[x_pos, y_pos])
    k = 0
    for i, employee1 in enumerate(positions.keys()):
        for j, employee2 in enumerate(positions.keys()):
            if i < j:
                lines[k].set_data([p[0] for p in positions[employee1][:num+1]],[p[1] for p in positions[employee2][:num+1]])
                k += 1


# Create an animation
ani = FuncAnimation(fig, update, frames=np.arange(min([len(pos) for pos in positions.values()])), repeat=False)
plt.xlim(0,12)
plt.ylim(0,12)
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.title("Employee Positions")

# Create an imageio gif
ani.save('employee_movement.gif', writer='pillow', fps=1)
