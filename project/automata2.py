import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from genalg import calculate_fitness2, pool_selector, crossover2
from automata import updater2i, gradient

if __name__ == "__main__":
    size = (16, 16)
    nx, ny = size
    space = np.zeros(size, dtype=int)
    ispace = np.copy(space)
    tgt = [14, 14]
    gradspace = gradient(size, tgt)

    rule = [[0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 0]]
    iters = 5
    gens = 400
    population = np.array([np.random.randint(2, size=(3, 3)) for _ in range(64)])
    counter = 0

    g = 0
    while g < gens:
        print("Gen ", g)
        fitnesses = calculate_fitness2(population, iters, size, space, gradspace, rule)
        # print("Avg fitness ", np.average(fitnesses), ". Max fitness ", np.max(fitnesses))
        parents = pool_selector(population, fitnesses, 56)
        offspring = crossover2(parents, 8)
        population = np.vstack((parents, offspring))
        for chromosome in population:
            if np.array_equal(np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]]), chromosome):
                print("Glider appeared")
                counter += 1
            if int(np.sum(gradspace)) == 400:
                space = ispace
                initial = np.hstack((np.vstack((chromosome, np.zeros(3, dtype=int))), np.zeros((4, 1), dtype=int)))
                rx, ry = 4, 4
                space[int(nx//2 - rx//2):int(nx//2 + rx//2), int(ny//2 - ry//2):int(ny//2 + ry//2)] = initial
                figure, ax = plt.subplots()
                img = ax.imshow(space, cmap="gray")
                visualiser = FuncAnimation(figure, updater2i, fargs=(img, ax, space, size, rule), frames=iters, repeat=False, interval=200)
                plt.show()
                g = gens
        g+=1

print("The glider appeared ", counter, "times")
            # for _ in range(iters):
            #     space = updater2(space, size, rule)

            # if np.transpose(np.nonzero(space)) == np.array([tgt, [tgt[0]+1, tgt[1]], [tgt[0], tgt[1]+1],[tgt[0]+1, tgt[1]+1]]):
            #     print("The solution is ", chromosome)
            #     break
            # if int(np.sum(gradspace)) == 4000:
            #     print("The solution is ", chromosome)
            #     break