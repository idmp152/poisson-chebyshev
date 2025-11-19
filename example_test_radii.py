import poisson
import numpy as np

SQUARE_SIZE = 200
MAX_TRIES = 30
WIDTH = 1250
HEIGHT = 1250

MAXIMIZE_TRIES = 30

def calculate_coverage(rectangle_points, width, height, square_size):
    total_area = width*height
    coverage_grid = np.zeros((width, height))
    for x, y in rectangle_points:
        coverage_grid[x:x+square_size, y:y+square_size] += 1

    coverage = np.sum(coverage_grid > 0) / total_area
    overlap = np.sum(coverage_grid > 1) / total_area
    return coverage, overlap

print(f"Calculating {WIDTH}x{HEIGHT} coverage with {SQUARE_SIZE} sized squares.\n")
for j in range(SQUARE_SIZE//2, SQUARE_SIZE+1):
    x, y = zip(*poisson.sample(j, MAX_TRIES, WIDTH, HEIGHT))
    rectangle_points = []
    for i in range(len(x)):
        square_size = SQUARE_SIZE
        lower_left_x = x[i] - square_size // 2
        lower_left_y = y[i] - square_size // 2

        rectangle_points.append((lower_left_x, lower_left_y))

    coverage, overlap = calculate_coverage(rectangle_points, WIDTH, HEIGHT, SQUARE_SIZE)
    print(f"Radius: {j} | Coverage: {coverage*100:.2f}% | Overlap: {overlap*100:.2f}% | Coverage/Overlap Ratio: {coverage/overlap:.2f} | Coverage minus Overlap Ratio: {(coverage - overlap)*100:.2f}")