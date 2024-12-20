import random

def function_to_optimize(x):
    return -x**2 + 4*x + 10  # Example: quadratic function

def initialize_population(pop_size, gene_length, bounds):
    return [[random.uniform(bounds[0], bounds[1]) for _ in range(gene_length)] for _ in range(pop_size)]

def evaluate_fitness(population):
    return [function_to_optimize(sum(genes)) for genes in population]

def select_parents(population, fitness):
    probabilities = [f / sum(fitness) for f in fitness]
    return random.choices(population, probabilities, k=len(population))

def crossover(parent1, parent2, crossover_rate):
    if random.random() < crossover_rate:
        point = random.randint(1, len(parent1) - 1)
        return parent1[:point] + parent2[point:]
    return parent1

def mutate(sequence, mutation_rate, bounds):
    return [
        gene + random.uniform(-1, 1) if random.random() < mutation_rate else gene
        for gene in sequence
    ]

def gene_expression(genes):
    return sum(genes)  # Example: sum of genes represents the functional solution

def gene_expression_algorithm(pop_size, gene_length, bounds, mutation_rate, crossover_rate, generations):
    population = initialize_population(pop_size, gene_length, bounds)
    best_solution = None
    best_fitness = float('-inf')

    for _ in range(generations):
        fitness = evaluate_fitness(population)
        if max(fitness) > best_fitness:
            best_fitness = max(fitness)
            best_solution = population[fitness.index(max(fitness))]

        parents = select_parents(population, fitness)
        offspring = [
            mutate(crossover(parents[i], parents[(i + 1) % len(parents)], crossover_rate), mutation_rate, bounds)
            for i in range(len(parents))
        ]
        population = offspring

    return gene_expression(best_solution), best_fitness

# Parameters
pop_size = 20
gene_length = 5
bounds = (-10, 10)
mutation_rate = 0.1
crossover_rate = 0.8
generations = 50

# Run Gene Expression Algorithm
best_solution, best_value = gene_expression_algorithm(pop_size, gene_length, bounds, mutation_rate, crossover_rate, generations)
print("Best Solution:", best_solution)
print("Maximum Value:", best_value)
