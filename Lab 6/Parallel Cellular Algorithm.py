import random
import numpy as np

def function_to_optimize(x):
    return -x**2 + 4*x + 10  # Example: quadratic function

def initialize_grid(grid_size, bounds):
    return np.random.uniform(bounds[0], bounds[1], grid_size)

def get_neighborhood(grid, x, y):
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1]:
                neighbors.append(grid[nx, ny])
    return neighbors

def update_cell_state(cell, neighbors):
    best_neighbor = max(neighbors, key=function_to_optimize)
    return (cell + best_neighbor) / 2

def parallel_cellular_algorithm(grid_size, bounds, iterations):
    grid = initialize_grid(grid_size, bounds)
    best_solution = None
    best_value = float('-inf')

    for _ in range(iterations):
        new_grid = grid.copy()

        for x in range(grid.shape[0]):
            for y in range(grid.shape[1]):
                neighbors = get_neighborhood(grid, x, y)
                new_grid[x, y] = update_cell_state(grid[x, y], neighbors)

                fitness = function_to_optimize(new_grid[x, y])
                if fitness > best_value:
                    best_value = fitness
                    best_solution = new_grid[x, y]

        grid = new_grid

    return best_solution, best_value

# Parameters
grid_size = (5, 5)  # 5x5 grid
bounds = (-10, 10)
iterations = 50

# Run Parallel Cellular Algorithm
best_solution, best_value = parallel_cellular_algorithm(grid_size, bounds, iterations)
print("Best Solution:", best_solution)
print("Maximum Value:", best_value)
