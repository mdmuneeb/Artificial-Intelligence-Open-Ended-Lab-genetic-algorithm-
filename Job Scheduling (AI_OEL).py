import random
jobs = 12
processing_times = [3, 2, 7, 5, 1, 6, 4, 8, 2, 1, 4, 5]
machines = 3  
population_size = 20
no_of_generations = 50
crossover_rate = 0.7
mutation_rate = 0.1

def calculate_makespan(schedule):
    machine_times = [0] * machines 
    for job in schedule:
        next_machine = machine_times.index(min(machine_times))
        machine_times[next_machine] += processing_times[job]
    return max(machine_times) 

def initialize_population():
    population = []  
    for i in range(population_size):  
        individual = random.sample(range(jobs), jobs) 
        population.append(individual) 
    return population


def fitness(schedule):
    return 1 / calculate_makespan(schedule)

def select_parents(population): # tournamnent selection
    parents = []
    for i in range(2):
        candidates = random.sample(population, 3)
        parents.append(max(candidates, key=fitness))
    return parents

def crossover(parent1, parent2):
    if random.random() > crossover_rate:
        return parent1[:]
    start, end = sorted(random.sample(range(jobs), 2))
    child = [None] * jobs
    child[start:end] = parent1[start:end]
    pointer = end
    for job in parent2:
        if job not in child:
            if pointer >= jobs:
                pointer = 0
            child[pointer] = job
            pointer += 1
    return child

def mutate(schedule):
    if random.random() < mutation_rate:
        i, j = random.sample(range(jobs), 2)
        schedule[i], schedule[j] = schedule[j], schedule[i]

def genetic_algorithm():
    population = initialize_population()
    for generation in range(no_of_generations):
        new_population = []
        for i in range(population_size):
            parent1, parent2 = select_parents(population)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)
        population = new_population
        best_schedule = min(population, key=calculate_makespan)
        # print(f"Generation {generation+1}: Best Makespan = {calculate_makespan(best_schedule)}")
    return best_schedule

best_solution = genetic_algorithm()
print("Best Schedule:", best_solution)
print("Minimum Makespan:", calculate_makespan(best_solution))


