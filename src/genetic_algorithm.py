import random
import copy
import pickle
import numpy

# Constants
GRID_SIZE = 5
PLANT_TYPES = [1, 2, 3]
POPULATION_SIZE = 1000
MAX_GENERATIONS = 100
MUTATION_RATE = 0.1

def generate_random_chromosome():
    # Generate a random chromosome (random matrix)
    chromosome = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            available_types = PLANT_TYPES.copy()
            chromosome[row][col] = random.choice(available_types)

    return chromosome

def calculate_fitness(chromosome):
    # Calculate the fitness by counting the number of adjacent fields with the same plant type
    fitness = 0
    appearances = [0,0,0]

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            plant_type = chromosome[row][col]

            # Check left neighbor
            if col > 0 and chromosome[row][col - 1] == plant_type:
                fitness += 1
            # Check top neighbor
            if row > 0 and chromosome[row - 1][col] == plant_type:
                fitness += 1

    
    for row in chromosome:
        appearances[0] = appearances[0] + row.count(1)
        appearances[1] = appearances[1] + row.count(2)
        appearances[2] = appearances[2] + row.count(3)

    for i in range(len(appearances)):
        if appearances[i] < 7 and appearances[i] > 9:
            fitness = fitness + abs(appearances[i]-8)
    return fitness

def selection(population):
    # Perform tournament selection to choose parents for reproduction
    tournament_size = 5
    parents = []

    for _ in range(len(population)):
        tournament = random.sample(population, tournament_size)
        tournament.sort(key=lambda chromosome: calculate_fitness(chromosome))
        parents.append(tournament[0])

    return parents

def crossover(parent1, parent2):
    # Perform single-point crossover to create two offspring
    crossover_point = random.randint(0, (GRID_SIZE*GRID_SIZE)-1)
    
    row = crossover_point // GRID_SIZE
    column = crossover_point % GRID_SIZE
    offspring1 = []
    offspring2 = []
    counter = 0
    while counter<row:
        offspring1.append(parent1[counter])
        offspring2.append(parent2[counter])
        counter += 1
    # The place, where the parents are 'cutten' is here
    offspring1.append(parent1[counter][:column] + parent2[counter][column:])
    offspring2.append(parent2[counter][:column] + parent1[counter][column:])

    while counter<GRID_SIZE-1:
        offspring1.append(parent2[counter])
        offspring2.append(parent1[counter])
        counter += 1

    return offspring1, offspring2


def genetic_algorithm():

    results = []
    population = [generate_random_chromosome() for _ in range(POPULATION_SIZE)]

    # Main loop
    for gen in range(MAX_GENERATIONS):
        parents = selection(population)
        offspring = []

        # Crossover
        for i in range(0, len(parents), 2):
            parent1 = parents[i]
            parent2 = parents[i + 1]
            child1, child2 = crossover(parent1, parent2)
            offspring.append(child1)
            offspring.append(child2)

        # Replacement
        population = offspring

        # Count best fitness of each population
        best_chromosome = min(population, key=lambda chromosome: calculate_fitness(chromosome))
        best_fitness = calculate_fitness(best_chromosome)
        results.append((copy.deepcopy(best_chromosome), best_fitness))
        if best_fitness == 0:
            break

    results.sort(key = lambda x: x[1])
    best_tuple = results[0]
    best_chromosome, best_fitness = best_tuple
    return best_chromosome

# Replacing numbers into plants:
def replace_numbers(number_matrix):
    return_matrix = number_matrix.copy()
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if number_matrix[row][col] == 1:
                return_matrix[row][col] = "carrot"
            elif number_matrix[row][col] == 2:
                return_matrix[row][col] = "potato"
            elif number_matrix[row][col] == 3:
                return_matrix[row][col] = "wheat"
            else:
                number_matrix[row][col] = "error"
    return return_matrix

# Make the matrix as a list:
def list_of_matrix(plant_matrix):
    return_list = []
    for i in range(len(plant_matrix)):
        return_list += plant_matrix[i]
    return return_list

# Run the genetic algorithm
best_solution = genetic_algorithm()

# Print the best solution found
print("Best Solution:")
for row in best_solution:
    print(row)
print("Best fitness: ", calculate_fitness(best_solution))
print("")

replaced_matrix = replace_numbers(best_solution)
print("Replaced Matrix:")
for row in replaced_matrix:
    print(row)
return_list = list_of_matrix(replaced_matrix)


with open("genetic_algorithm_matrix.pkl", "wb") as file:
    pickle.dump(return_list, file)