import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from genalg import calculate_fitness1, calculate_fitness2, pool_selector, crossover1, crossover2
from automata import updater1, updater2, updater2i, gradient
from time import sleep

if __name__ == "__main__":
    choice = int(input("Enter 1 or 2 for 1D or 2D automaton "))
    if choice == 1:
        N = 100
        space = np.random.randint(2, size=N)
        # print("Initial space is ", space)
        ispace = np.copy(space)
        generations = 20

        population = np.array([np.random.randint(2, size=3) for _ in range(10)])
        # print("Initial population is ", population)
        t = 1
        while t < 10:
            fitnesses = calculate_fitness1(population, generations, N, space)
            parents = pool_selector(population, fitnesses, 3)
            offspring = crossover1(parents, 2)
            population = np.vstack((parents, offspring))
            # print("Population is ", population)
            solutions = []
            for chromosome in population:
                space = ispace
                for _ in range(1, generations):
                    space = updater1(space, N, chromosome)
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
    else:
        size = (40, 40)
        nx, ny = size
        space = np.zeros(size, dtype=int)
        ispace = np.zeros(size, dtype=int)
        tgt = [1, 1]
        gradspace = gradient(size, tgt)
        # print(gradspace)

        rule = [[0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 0]]
        iters = 30
        gens = 20
        population = np.array([np.random.randint(2, size=(4, 4)) for _ in range(64)])
        soln = np.zeros(size, dtype=int)

        g = 0
        while g < gens:
            print("Gen ", g, "running")
            space = ispace
            fitnesses = calculate_fitness2(population, iters, size, space, gradspace, rule)
            # print("Avg fitness ", np.average(fitnesses), ". Max fitness ", np.max(fitnesses))
            parents = pool_selector(population, fitnesses, 48)
            offspring = crossover2(parents, 16)
            population = np.vstack((parents, offspring))
            for chromosome in population:
                space = ispace
                rx, ry = 4, 4
                space[int(nx//2 - rx//2):int(nx//2 + rx//2), int(ny//2 - ry//2):int(ny//2 + ry//2)] = chromosome
                for _ in range(iters):
                    space = updater2(space, size, rule)
                if space[tgt[0], tgt[1]] == 1:
                    print("Solution\n", chromosome)
                    soln = np.copy(chromosome)
                    g = gens
                    break
            g+=1

        if np.any(soln) > 0:
            space = ispace
            rx, ry = 4, 4
            space[int(nx//2 - rx//2):int(nx//2 + rx//2), int(ny//2 - ry//2):int(ny//2 + ry//2)] = soln
            sleep(4)
            figure, ax = plt.subplots()
            img = ax.imshow(space, cmap="gray")
            visualiser = FuncAnimation(figure, updater2i, fargs=(img, ax, space, size, rule), frames=iters, repeat=False, interval=600)
            plt.show()