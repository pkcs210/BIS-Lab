import random

def function_to_optimize(x):
    return -x**2 + 4*x + 10  # Example: quadratic function

def initialize_population(num_wolves, bounds):
    return [random.uniform(bounds[0], bounds[1]) for _ in range(num_wolves)]

def update_position(wolf, alpha, beta, delta, a, bounds):
    r1, r2 = random.random(), random.random()
    A1 = 2 * a * r1 - a
    C1 = 2 * r2
    D_alpha = abs(C1 * alpha - wolf)
    X1 = alpha - A1 * D_alpha

    r1, r2 = random.random(), random.random()
    A2 = 2 * a * r1 - a
    C2 = 2 * r2
    D_beta = abs(C2 * beta - wolf)
    X2 = beta - A2 * D_beta

    r1, r2 = random.random(), random.random()
    A3 = 2 * a * r1 - a
    C3 = 2 * r2
    D_delta = abs(C3 * delta - wolf)
    X3 = delta - A3 * D_delta

    new_position = (X1 + X2 + X3) / 3
    return max(bounds[0], min(bounds[1], new_position))

def grey_wolf_optimizer(num_wolves, bounds, iterations):
    wolves = initialize_population(num_wolves, bounds)
    fitness = [function_to_optimize(wolf) for wolf in wolves]

    alpha, beta, delta = sorted(wolves, key=function_to_optimize, reverse=True)[:3]

    for t in range(iterations):
        a = 2 - t * (2 / iterations)

        for i in range(num_wolves):
            wolves[i] = update_position(wolves[i], alpha, beta, delta, a, bounds)
            fitness[i] = function_to_optimize(wolves[i])

        alpha, beta, delta = sorted(wolves, key=function_to_optimize, reverse=True)[:3]

    return alpha, function_to_optimize(alpha)

# Parameters
num_wolves = 20
bounds = (-10, 10)
iterations = 50

# Run Grey Wolf Optimizer
best_solution, best_value = grey_wolf_optimizer(num_wolves, bounds, iterations)
print("Best Solution:", best_solution)
print("Maximum Value:", best_value)
