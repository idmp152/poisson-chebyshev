import random
from math import ceil, floor

def sample(radius: int, max_tries: int, width: int, height: int):
    cell_size = radius 
    cell_width = ceil(width/cell_size) + 1
    cell_height = ceil(height/cell_size) + 1

    grid = [[None for _ in range(cell_width)] for _ in range(cell_height)]

    points = []
    active = []

    current_point = (random.randint(0, width), random.randint(0, height))
    points.append(current_point)
    active.append(current_point)

    grid_insert(grid, current_point, cell_size)
    while active:
        current_point_idx = random.randint(0, len(active) - 1)
        current_point = active[current_point_idx]
        found = False

        for _ in range(max_tries):
            rpoint = generate_rpoint(current_point, radius)

            if not is_point_valid(rpoint, width, height, cell_width, cell_height, cell_size, grid, radius):
                continue

            found = True
            points.append(rpoint)
            active.append(rpoint)
            grid_insert(grid, rpoint, cell_size)

        if not found:
            active.pop(current_point_idx)
    

    return points

def generate_rpoint(point: tuple[int, int], radius: int):
    low_left_outer = (point[0] - radius*2, point[1] - radius*2)
    high_right_outer = (point[0] + radius * 2, point[1] + radius*2)
    low_left_inner = (point[0] - radius, point[1] - radius)
    high_right_inner = (point[0] + radius, point[1] + radius)

    while True:
        x, y = (random.randint(low_left_outer[0], high_right_outer[0]), random.randint(low_left_outer[1], high_right_outer[1]))
        if not (x < high_right_inner[0] and x > low_left_inner[0] and y < high_right_inner[1] and y > low_left_inner[1]):
            return (x, y)

def grid_insert(grid: list[list], point: tuple[int, int], cell_size: float):
    grid[floor(point[0] / cell_size)][floor(point[1] / cell_size)] = point

def cheb_dist(p, q):
    return max(abs(px - qx) for px, qx in zip(p, q))

def is_point_valid(rpoint: tuple[int, int], width: int, height: int, cell_width: int, cell_height: int, cell_size: float, grid: list[list], radius: int):
    if (rpoint[0] < 0 or rpoint[0] > width or rpoint[1] < 0 or rpoint[1] > height):
        return False
    
    x = floor(rpoint[0] / cell_size)
    y = floor(rpoint[1] / cell_size)
    i_min = max(x - 1, 0)
    i_max = min(x + 1, cell_width - 1)
    j_min = max(y - 1, 0)
    j_max = min(y + 1, cell_height - 1)

    for i in range(i_min, i_max + 1):
        for j in range(j_min, j_max + 1):
            if grid[i][j] and (cheb_dist(rpoint, grid[i][j]) < radius):
                return False
            
    return True
