import random
import math

def function_to_optimize(x):
    return -x**2 + 4*x + 10  # Example: quadratic function

def initialize_population(size, bounds):
    return [random.uniform(bounds[0], bounds[1]) for _ in range(size)]

def evaluate_fitness(population):
    return [function_to_optimize(ind) for ind in population]

def select_parents(population, fitness):
    total_fitness = sum(fitness)
    probabilities = [f / total_fitness for f in fitness]
    return random.choices(population, probabilities, k=2)

def crossover(parent1, parent2):
    return (parent1 + parent2) / 2

def mutate(individual, mutation_rate, bounds):
    if random.random() < mutation_rate:
        return random.uniform(bounds[0], bounds[1])
    return individual

def genetic_algorithm(pop_size, bounds, mutation_rate, crossover_rate, generations):
    population = initialize_population(pop_size, bounds)

    for _ in range(generations):
        fitness = evaluate_fitness(population)
        new_population = []

        for _ in range(pop_size):
            parent1, parent2 = select_parents(population, fitness)
            if random.random() < crossover_rate:
                offspring = crossover(parent1, parent2)
            else:
                offspring = random.choice([parent1, parent2])
            offspring = mutate(offspring, mutation_rate, bounds)
            new_population.append(offspring)

        population = new_population

    best_individual = max(population, key=function_to_optimize)
    return best_individual

# Parameters
population_size = 20
bounds = (-10, 10)
mutation_rate = 0.1
crossover_rate = 0.7
generations = 50

# Run Genetic Algorithm
best_solution = genetic_algorithm(population_size, bounds, mutation_rate, crossover_rate, generations)
print("Best Solution:", best_solution)
print("Maximum Value:", function_to_optimize(best_solution))
