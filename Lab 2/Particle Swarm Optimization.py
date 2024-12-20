import random

def function_to_optimize(x):
    return -x**2 + 4*x + 10  # Example: quadratic function

def initialize_particles(num_particles, bounds):
    positions = [random.uniform(bounds[0], bounds[1]) for _ in range(num_particles)]
    velocities = [random.uniform(-1, 1) for _ in range(num_particles)]
    return positions, velocities

def update_velocity(velocity, position, personal_best, global_best, w, c1, c2):
    inertia = w * velocity
    cognitive = c1 * random.random() * (personal_best - position)
    social = c2 * random.random() * (global_best - position)
    return inertia + cognitive + social

def update_position(position, velocity, bounds):
    new_position = position + velocity
    return max(bounds[0], min(bounds[1], new_position))

def particle_swarm_optimization(num_particles, bounds, w, c1, c2, iterations):
    positions, velocities = initialize_particles(num_particles, bounds)
    personal_bests = positions[:]
    global_best = max(positions, key=function_to_optimize)

    for _ in range(iterations):
        for i in range(num_particles):
            velocities[i] = update_velocity(velocities[i], positions[i], personal_bests[i], global_best, w, c1, c2)
            positions[i] = update_position(positions[i], velocities[i], bounds)

            if function_to_optimize(positions[i]) > function_to_optimize(personal_bests[i]):
                personal_bests[i] = positions[i]

        global_best = max(personal_bests, key=function_to_optimize)

    return global_best

# Parameters
num_particles = 20
bounds = (-10, 10)
w = 0.5  # inertia weight
c1 = 1.5  # cognitive coefficient
c2 = 1.5  # social coefficient
iterations = 50

# Run Particle Swarm Optimization
best_solution = particle_swarm_optimization(num_particles, bounds, w, c1, c2, iterations)
print("Best Solution:", best_solution)
print("Maximum Value:", function_to_optimize(best_solution))
