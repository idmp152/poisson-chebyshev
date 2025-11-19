import poisson
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

SQUARE_SIZE = 13 # 13x13 squares 
RADIUS = 8 # With approximate Chebyshev distance of 8 between centers
MAX_TRIES = 30 # Maximum tries for generating each neighbouring point. Decrease for less accuracy and higher performance. 
WIDTH = 625 # Width of the area to sample.
HEIGHT = 625 # Height of the area to sample.

x, y = zip(*poisson.sample(RADIUS, MAX_TRIES, WIDTH, HEIGHT))

fig, ax = plt.subplots()

def calculate_coverage(rectangle_points, width, height, square_size):
    total_area = width*height
    coverage_grid = np.zeros((width, height))
    for x, y in rectangle_points:
        coverage_grid[x:x+square_size, y:y+square_size] += 1

    coverage = np.sum(coverage_grid > 0) / total_area
    overlap = np.sum(coverage_grid > 1) / total_area
    return coverage, overlap

ax.set_aspect('equal', adjustable='box')
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.scatter(x, y, 1)
rectangle_points = []
for i in range(len(x)):
    square_size = SQUARE_SIZE
    lower_left_x = x[i] - square_size // 2
    lower_left_y = y[i] - square_size // 2

    rectangle_points.append((lower_left_x, lower_left_y))

    square = patches.Rectangle(
        (lower_left_x, lower_left_y),
        square_size,
        square_size,
        linewidth=0.5,
        edgecolor='black',
        facecolor='blue',
        alpha=0.2
    )

    ax.add_patch(square)

coverage, overlap = calculate_coverage(rectangle_points, WIDTH, HEIGHT, SQUARE_SIZE)
ax.set_title(f"Coverage: {coverage*100:.2f}%\nOverlap: {overlap*100:.2f}%")
plt.show()