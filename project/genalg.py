import numpy as np
from math import floor
from automata1 import updater

def calculate_fitness(population, generations, size, space):
    fitnesses = []
    for chromosome in population:
        rule = chromosome
        for _ in range(generations):
            space = updater(space, size, rule)
        fitnesses.append(np.sum(space))
    return np.array(fitnesses)

def pool_selector(population, fitnesses, number):
    parents = []
    for _ in range(number):
        max_fitness = np.where(fitnesses == np.max(fitnesses))[0][0]
        parents.append(population[max_fitness])
        fitnesses[max_fitness] = -9999
    return np.array(parents)

def crossover(parents, number):
    offspring = np.empty((number, np.shape(parents)[1]), dtype=int)
    point = floor(len(parents[0]) / 2)
    for n in range(number):
        offspring[n, 0:point] = parents[n, 0:point]
        offspring[n, point:] = parents[-n-1, point:]
    offspring = mutation(np.array(offspring))
    return offspring

def mutation(offspring):
    switch = {0: 1, 1: 0}
    for o in range(len(offspring)):
        probability = np.random.uniform(0, 1)
        if probability > 0.9:
            idx = np.random.randint(3, dtype=int)
            # print("Offspring array is ", offspring)
            # print("Index is ", (o, idx))
            # print("Offspring is ", offspring[o, idx])
            offspring[o, idx] = switch[offspring[o, idx]]
    return offspring