import math

#task1

def l2_norm(vector):
    sum_of_squares = sum([x ** 2 for x in vector])
    return math.sqrt(sum_of_squares)

def l1_norm(vector):
    return sum([abs(x) for x in vector])

def l_infinity_norm(vector):
    return max([abs(x) for x in vector])

def lp_norm(vector, p):
    return sum([abs(x) ** p for x in vector]) ** (1/p)

def l1_norm(vector):
    return sum([abs(x) for x in vector])

def l_infinity_norm(vector):
    return max([abs(x) for x in vector])

def l3_norm(vector):
    return sum([abs(x) ** 3 for x in vector]) ** (1/3)

def l4_norm(vector):
    return sum([abs(x) ** 4 for x in vector]) ** (1/4)

def lp_norm(vector, p):
    return sum([abs(x) ** p for x in vector]) ** (1/p)

def l0_norm(vector):
    return len([x for x in vector if x != 0])

#task 2

import random
import matplotlib.pyplot as plt

# Define the number of balls and the range of x and y coordinates
num_balls = 20
x_range = (-5, 5)
y_range = (-5, 5)

# Initialize an empty list to store ball coordinates and colors
balls = []

# Generate random coordinates and colors for the balls
for _ in range(num_balls):
    x_center = random.uniform(x_range[0] + 1, x_range[1] - 1)  # Ensure balls are within the range
    y_center = random.uniform(y_range[0] + 1, y_range[1] - 1)
    color = (random.random(), random.random(), random.random())  # RGB color tuple
    balls.append((x_center, y_center, color))

# Create a plot
fig, ax = plt.subplots()

# Plot the unit balls
for ball in balls:
    x_center, y_center, color = ball
    circle = plt.Circle((x_center, y_center), 1, color=color, fill=True)
    ax.add_patch(circle)

# Set axis limits and labels
ax.set_xlim(x_range)
ax.set_ylim(y_range)
ax.set_aspect('equal')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Randomly Colored Unit Balls')

# Show the plot
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()
plt.show()
