import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from automata import transition2

def updater(frame_number, img, space, size, rule):
    tempspace = np.copy(space)
    for i in range(size[0]):
        for j in range(size[1]):
            try:
                neighbours = space[i, j+1] + space[i, j-1] + space[i+1, j] + space[i-1, j] + space[i+1, j+1] + space[i-1, j-1] + space[i+1, j-1] + space[i-1, j+1]
                tempspace[i, j] = transition2(neighbours, rule, space[i, j])
            except IndexError:
                if tempspace[i, j] == 1:
                    tempspace[i, j] = 0 if np.random.uniform() > 0.9 else 1
                else:
                    tempspace[i, j] = 1 if np.random.uniform() > 0.95 else 0
    img.set_data(tempspace)
    space[:] = tempspace[:] 
    return img

if __name__ == "__main__":
    size = (38, 38)
    nx, ny = size
    space = np.zeros(size, dtype=int)
    rx, ry = 12, 14
    space[int(nx//2 - rx//2):int(nx//2 + rx//2), int(ny//2 - ry//2):int(ny//2 + ry//2)] = np.random.randint(0, 2, (rx, ry))
    rule = [[0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0, 0, 0]]
    iters = 120
    figure, ax = plt.subplots()
    img = ax.imshow(space, cmap="gray")
    visualiser = FuncAnimation(figure, updater, fargs=(img, space, size, rule), frames=iters, repeat=False, interval=30)
    plt.show()