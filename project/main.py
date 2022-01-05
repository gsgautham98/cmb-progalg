import numpy as np
import matplotlib.pyplot as plt
from automata1 import updater
from genalg import calculate_fitness, pool_selector, crossover

if __name__ == "__main__":
    N = 100
    space = np.random.randint(2, size=N)
    print("Initial space is ", space)
    ispace = np.copy(space)
    generations = 20

    population = np.array([np.random.randint(2, size=3) for _ in range(10)])
    # print("Initial population is ", population)
    t = 1
    while t < 10:
        fitnesses = calculate_fitness(population, generations, N, space)
        parents = pool_selector(population, fitnesses, 3)
        offspring = crossover(parents, 2)
        population = np.vstack((parents, offspring))
        # print("Population is ", population)
        solutions = []
        for chromosome in population:
            space = ispace
            for _ in range(1, generations):
                space = updater(space, N, chromosome)
                if np.all(space) == 1:
                    solutions.append(chromosome)
                    break
        t+=1
    print("The solution(s) are\n", np.unique(solutions, axis=0))

    # fig, ax = plt.subplots()
    # img = ax.imshow(np.array(spaces_stack), cmap="gray")
    # plt.title("Cellular automata visualisation")
    # plt.xlabel("Chromosome " + str(chromosome))
    # plt.show()