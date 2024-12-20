import random
import math

def function_to_optimize(x):
    return -x**2 + 4*x + 10  # Example: quadratic function

def levy_flight():
    beta = 1.5
    sigma = (math.gamma(1 + beta) * math.sin(math.pi * beta / 2) /
             (math.gamma((1 + beta) / 2) * beta * 2**((beta - 1) / 2)))**(1 / beta)
    u = random.gauss(0, sigma)
    v = random.gauss(0, 1)
    return u / abs(v)**(1 / beta)

def initialize_nests(num_nests, bounds):
    return [random.uniform(bounds[0], bounds[1]) for _ in range(num_nests)]

def abandon_worst_nests(nests, fitness, discovery_rate, bounds):
    num_abandoned = int(len(nests) * discovery_rate)
    worst_indices = sorted(range(len(fitness)), key=lambda i: fitness[i])[:num_abandoned]
    for i in worst_indices:
        nests[i] = random.uniform(bounds[0], bounds[1])
    return nests

def cuckoo_search(num_nests, bounds, discovery_rate, iterations):
    nests = initialize_nests(num_nests, bounds)
    fitness = [function_to_optimize(nest) for nest in nests]
    best_nest = nests[fitness.index(max(fitness))]

    for _ in range(iterations):
        for i in range(num_nests):
            step = levy_flight()
            new_nest = nests[i] + step
            new_nest = max(bounds[0], min(bounds[1], new_nest))

            if function_to_optimize(new_nest) > fitness[i]:
                nests[i] = new_nest
                fitness[i] = function_to_optimize(new_nest)

        best_nest = nests[fitness.index(max(fitness))]
        nests = abandon_worst_nests(nests, fitness, discovery_rate, bounds)
        fitness = [function_to_optimize(nest) for nest in nests]

    return best_nest, function_to_optimize(best_nest)

# Parameters
num_nests = 20
bounds = (-10, 10)
discovery_rate = 0.25
iterations = 50

# Run Cuckoo Search
best_solution, best_value = cuckoo_search(num_nests, bounds, discovery_rate, iterations)
print("Best Solution:", best_solution)
print("Maximum Value:", best_value)
