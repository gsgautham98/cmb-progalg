import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from genalg import calculate_fitness1, calculate_fitness2, calculate_fitness3, pool_selector, crossover1, crossover2            # Genetic algorithm functions
from automata import gradient, updater, updater1, updater2, updater2_animated, updater3, updater3_animated           # Cellular automata functions
from time import sleep

if __name__ == "__main__":

    # Welcome message #

    welcome = '''\nEvolving cellular automata with genetic algorithms \n
    Please choose one of the following \n
    1 Majority problem in a 1D cellular automaton\n
    2 50-50 problem in a 2D cellular automaton\n
    3 Directing dynamcs in the Game of Life\n
    4 Maze-like 2D layout generator\n
    Enter choice number '''

    choice = int(input(welcome).strip())

    # Majority problem in 1D cellular automaton #

    if choice == 1:
        size = 100
        space = np.zeros(size, dtype=int)
        rx = 10
        space[size//2 - rx//2:size//2 + rx//2] = np.random.randint(0, 2, rx, dtype=int)         # Randomising select part of the grid space
        ispace = np.copy(space)
        gens = 20           # Generations of genetic algorithm           
        iters = 15          # Generations of cellular automaton

        population = np.array([np.random.randint(2, size=3) for _ in range(8)])         # Initial random population of chromosomes

        g = 1
        while g < gens:
            print("\nGen ", g, "running")
            fitnesses = calculate_fitness1(population, iters, size, space)          # Calculation of fitness
            parents = pool_selector(population, fitnesses, 6)           # Selection of parents
            offspring = crossover1(parents, 2)          # Production of offspring
            population = np.vstack((parents, offspring))            # New population
            solved = False          # To check if solved
            for chromosome in population:
                space = np.copy(ispace)
                stack = np.copy(ispace)
                checks = []
                for _ in range(1, iters):           # Evolving the cellular automaton
                    space = updater1(space, size, chromosome)
                    stack = np.vstack((stack, space))
                    if np.sum(space) == size // 2:
                        print("A solution is ", chromosome)
                        solved = True
                        break
                if solved:          # In case it is solved
                    sleep(2)
                    fig, ax = plt.subplots()
                    img = ax.imshow(stack, cmap="gray")
                    plt.title("Visualisation of 1D cellular automaton")
                    plt.show()
                    g = gens
                    break
            g+=1
        
        if not solved:
            print("Unable to solve for given initial space within ", gens, "generations of the genetic algorithm")


    # 50-50 problem in 2D cellular automaton #

    elif choice == 2:
        size = (50, 50)
        nx, ny = size
        space = np.zeros(size, dtype=int)
        rx, ry = 10, 10
        space[int(nx//2 - rx//2):int(nx//2 + rx//2), int(ny//2 - ry//2):int(ny//2 + ry//2)] = np.random.randint(0, 2, (rx, ry))
        ispace = np.copy(space)

        iters = 28
        gens = 40
        population = np.array([np.random.randint(2, size=9) for _ in range(80)])

        g = 1
        while g < gens:
            print("\nGen ", g, "running")
            space = np.copy(ispace)
            fitnesses = calculate_fitness3(population, iters, size, space)
            print("Avg fitness ", np.average(fitnesses), ". Max fitness ", np.max(fitnesses))
            parents = pool_selector(population, fitnesses, 64)
            offspring = crossover1(parents, 16)
            population = np.vstack((parents, offspring))
            solved = False
            for chromosome in population:
                space = np.copy(ispace)
                for _ in range(iters):
                    space = updater3(space, size, chromosome)
                    if np.sum(space) == (size[0] * size[1]) // 2:
                        solved = True
                        soln = np.copy(chromosome)
                        i = _
                        print("A solution for the given initial state is ", soln)
                        break
                if solved:
                    g = gens
                    break
            g+=1
        
        if not solved:
            print("Unable to solve for given initial space within ", gens, "generations of the genetic algorithm")
        else:
            sleep(2)
            space = np.copy(ispace)
            figure, ax = plt.subplots()
            img = ax.imshow(space, cmap="gray")
            visualiser = FuncAnimation(figure, updater3_animated, fargs=(img, ax, space, size, soln), frames=i, repeat=False, interval=600)
            plt.show()


    # Directing dynmaics in in the Game of Life #

    elif choice == 3:
        size = (40, 40)
        nx, ny = size
        space = np.zeros(size, dtype=int)
        ispace = np.zeros(size, dtype=int)
        tgt = [1, 1]
        gradspace = gradient(size, tgt)

        rule = [[0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 0]]
        iters = 40
        gens = 100
        population = np.array([np.random.randint(2, size=(4, 4)) for _ in range(100)])
        soln = np.zeros(size, dtype=int)

        g = 1
        while g < gens:
            print("\nGen ", g, "running")
            space = np.copy(ispace)
            fitnesses = calculate_fitness2(population, iters, size, space, gradspace, rule)
            print("Avg fitness ", np.average(fitnesses), ". Max fitness ", np.max(fitnesses))
            parents = pool_selector(population, fitnesses, 90)
            offspring = crossover2(parents, 10)
            population = np.vstack((parents, offspring))
            for chromosome in population:
                space = np.copy(ispace)
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
            space = np.copy(ispace)
            rx, ry = 4, 4
            space[int(nx//2 - rx//2):int(nx//2 + rx//2), int(ny//2 - ry//2):int(ny//2 + ry//2)] = soln
            sleep(2)
            figure, ax = plt.subplots()
            img = ax.imshow(space, cmap="gray")
            visualiser = FuncAnimation(figure, updater2_animated, fargs=(img, ax, space, size, rule), frames=iters, repeat=False, interval=600)
            plt.show()
        else:
            print("Unable to solve for given initial space within ", gens, "generations of the genetic algorithm")


    # Maze-like 2D layout generator #

    elif choice == 4:
        size = (32, 32)
        nx, ny = size
        space = np.zeros(size, dtype=int)
        rx, ry = 8, 10
        space[int(nx//2 - rx//2):int(nx//2 + rx//2), int(ny//2 - ry//2):int(ny//2 + ry//2)] = np.random.randint(0, 2, (rx, ry))
        rule = [[0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0, 0, 0]]
        iters = 140

        figure, ax = plt.subplots()
        img = ax.imshow(space, cmap="gray")
        visualiser = FuncAnimation(figure, updater, fargs=(img, space, size, rule), frames=iters, repeat=False, interval=50)
        # visualiser.save("clips/maze-generator.mp4", fps=20)
        plt.show()

    else:
        print("Incorrect input")