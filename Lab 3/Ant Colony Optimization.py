import random
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def initialize_pheromones(num_cities, initial_pheromone):
    return [[initial_pheromone for _ in range(num_cities)] for _ in range(num_cities)]

def probability(pheromone, heuristic, alpha, beta):
    return (pheromone**alpha) * (heuristic**beta)

def construct_solution(ant, cities, pheromones, alpha, beta):
    unvisited = set(range(len(cities)))
    current_city = ant
    unvisited.remove(current_city)
    path = [current_city]

    while unvisited:
        probabilities = []
        for next_city in unvisited:
            pheromone = pheromones[current_city][next_city]
            heuristic = 1 / calculate_distance(cities[current_city], cities[next_city])
            probabilities.append(probability(pheromone, heuristic, alpha, beta))

        total = sum(probabilities)
        probabilities = [p / total for p in probabilities]
        next_city = random.choices(list(unvisited), weights=probabilities, k=1)[0]
        path.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    return path

def update_pheromones(pheromones, all_paths, cities, evaporation_rate):
    for i in range(len(pheromones)):
        for j in range(len(pheromones)):
            pheromones[i][j] *= (1 - evaporation_rate)

    for path in all_paths:
        distance = sum(calculate_distance(cities[path[i]], cities[path[i + 1]]) for i in range(len(path) - 1))
        pheromone_deposit = 1 / distance
        for i in range(len(path) - 1):
            pheromones[path[i]][path[i + 1]] += pheromone_deposit
            pheromones[path[i + 1]][path[i]] += pheromone_deposit

def total_distance(path, cities):
    return sum(calculate_distance(cities[path[i]], cities[path[i + 1]]) for i in range(len(path) - 1))

def ant_colony_optimization(cities, num_ants, alpha, beta, evaporation_rate, initial_pheromone, iterations):
    num_cities = len(cities)
    pheromones = initialize_pheromones(num_cities, initial_pheromone)
    best_path = None
    best_distance = float('inf')

    for _ in range(iterations):
        all_paths = [construct_solution(ant % num_cities, cities, pheromones, alpha, beta) for ant in range(num_ants)]
        update_pheromones(pheromones, all_paths, cities, evaporation_rate)

        for path in all_paths:
            distance = total_distance(path, cities)
            if distance < best_distance:
                best_path = path
                best_distance = distance

    return best_path, best_distance

# Example Usage
cities = [(0, 0), (2, 2), (2, 0), (0, 2), (1, 1)]
num_ants = 10
alpha = 1
beta = 2
evaporation_rate = 0.5
initial_pheromone = 1
iterations = 100

best_path, best_distance = ant_colony_optimization(cities, num_ants, alpha, beta, evaporation_rate, initial_pheromone, iterations)
print("Best Path:", best_path)
print("Shortest Distance:", best_distance)
