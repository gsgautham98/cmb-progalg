import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def gradient(s, r, c, t):
    g = np.zeros((len(s), len(s[0])), dtype=float)
    for i in range(r):
        for j in range(c):
            ed = ((i - t[0]) ** 2 + (j - t[1]) ** 2) ** 0.5
            g[i, j] = 1 / (ed + 0.15)
    return g

def updater(frame_number, img, space, fitnesses, maximum):
    global point
    for i in range(point[0] - 1, point[0] + 2, 1):
        for j in range(point[1] - 1, point[1] + 2, 1):
            try:
                if fitnesses[i, j] > maximum:
                    maximum = fitnesses[i, j]
                    temp = (i, j)
            except IndexError:
                continue
    space[point] = 0.2
    space[temp] = 1
    point = temp
    img.set_data(space)
    ax.set_xlabel(frame_number)
    return img

if __name__ == "__main__":
    space = np.zeros((50, 50))
    source = (np.random.randint(0, 49), np.random.randint(0, 49))
    target = (np.random.randint(0, 49), np.random.randint(0, 49))
    space[source] = 0.8
    space[target] = 1
    fitnesses = gradient(space, len(space), len(space[0]), target)
    N = 100
    point = source
    figure, ax = plt.subplots()
    img = ax.imshow(space, cmap = "gray")
    visualiser = FuncAnimation(figure, updater, fargs=(img, space, fitnesses, 0,), frames=N, repeat=False, interval=100)
    plt.title("Directed cellular automaton dynamics")
    plt.show()