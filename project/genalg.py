import numpy as np
from math import ceil, floor
from automata import updater1, updater2

def calculate_fitness1(population, generations, size, space):
    fitnesses = []
    for chromosome in population:
        for _ in range(generations):
            space = updater1(space, size, chromosome)
        fitnesses.append(np.sum(space))
    return np.array(fitnesses)

def calculate_fitness2(population, iterations, size, space, funcspace, rule):
    nx, ny = size
    fitnesses = []
    for chromosome in population:
        # initial = np.hstack((np.vstack((chromosome, np.zeros(3, dtype=int))), np.zeros((4, 1), dtype=int)))
        rx, ry = 4, 4
        space[int(nx//2 - rx//2):int(nx//2 + rx//2), int(ny//2 - ry//2):int(ny//2 + ry//2)] = chromosome
        for _ in range(iterations):
            space = updater2(space, size, rule)
        idxs = np.transpose(np.nonzero(space))
        fitnesses.append(np.sum(np.array([funcspace[tuple(i)] for i in idxs])))
    return np.array(fitnesses)

def pool_selector(population, fitnesses, number):
    parents = []
    for _ in range(number):
        max_fitness = np.where(fitnesses == np.max(fitnesses))[0][0]
        parents.append(population[max_fitness])
        fitnesses[max_fitness] = -99999
    return np.array(parents)

def crossover1(parents, number):
    offspring = np.empty((number, np.shape(parents)[1]), dtype=int)
    midway = floor(len(parents[0]) / 2)
    for n in range(number):
        offspring[n, 0:midway+1] = parents[n, 0:midway+1]
        offspring[n, midway+1:] = parents[-n-1, midway+1:]
    offspring = mutation1(np.array(offspring))
    return offspring

def crossover2(parents, number):
    offspring = np.empty((number, np.shape(parents)[1], np.shape(parents)[2]), dtype=int)
    breakoff = floor(np.shape(parents[0])[0] / 2)
    for n in range(number):
        offspring[n][0:breakoff+1, :] = parents[n][0:breakoff+1, :]
        offspring[n][breakoff+1:, :] = parents[-n-1][breakoff+1:, :]
    offspring = mutation2(np.array(offspring))
    return offspring

def mutation1(offspring):
    switch = {0: 1, 1: 0}
    for o in range(len(offspring)):
        trial = np.random.uniform(0, 1)
        if trial > 0.9:
            idx = np.random.randint(3, dtype=int)
            # print("Offspring array is ", offspring)
            # print("Index is ", (o, idx))
            # print("Offspring is ", offspring[o, idx])
            offspring[o, idx] = switch[offspring[o, idx]]
    return offspring

def mutation2(offspring):
    switch = {0: 1, 1: 0}
    for n in range(len(offspring)):
        trial = np.random.uniform(0, 1)
        if trial > 0.98:
            idx1, idx2 = np.random.randint(3, size=2, dtype=int)
            offspring[n][idx1, idx2] = switch[offspring[n][idx1, idx2]]
    return offspring