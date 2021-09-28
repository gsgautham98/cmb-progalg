import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def random_grid(cells_x, cells_y):
    initial_space = np.array()
    for i in range(cells_x):
        np.append(np.random.randint(0, 2, cells_y))
    return initial_space

def update_anime_func(frame_number, img, gsp):
    for i in range(32):
        for j in range(32):
            try:
                neighbours = gsp[i][j+1] + gsp[i][j-1] + gsp[i-1][j] + gsp[i-1][j-1] + gsp[i-1][j+1] + gsp[i+1][j+1] + gsp[i+1][j] + gsp[i+1][j-1]
            except IndexError:
                pass
            if neighbours == 3 and gsp[i][j] == 0:
                gsp[i][j] = 1
            elif neighbours in [2, 3] and gsp[i][j] == 1:
                gsp[i][j] = 1
            else:
                gsp[i][j] = 0
    img.set_data(gsp)
    return img

with open("gamespace", "r") as gsp_file:
    initialise_space = []
    for x in [line.strip().split() for line in gsp_file.read().strip().split("\n")]:
        initialise_space.append([int(i) for i in list(x[0])])

gsp = np.array(initialise_space)
figure, ax = plt.subplots()
img = ax.imshow(gsp, cmap="gray")
anime = FuncAnimation(figure, update_anime_func, fargs=(img, gsp,), frames=500, repeat=False, interval=200)
plt.show()