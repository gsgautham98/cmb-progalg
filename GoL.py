import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def random_grid(cells_x, cells_y):
    initialise_space = []
    for _ in range(cells_x):
        initialise_space.append(np.random.randint(0, 2, cells_y))
    return initialise_space

def update_anime_func(frame_number, img, gsp, rows, columns):
    temp_gsp = gsp.copy()
    for i in range(1, rows-1):
        for j in range(1, columns-1):
            neighbours = gsp[i][j+1] + gsp[i][j-1] + gsp[i-1][j] + gsp[i-1][j-1] + gsp[i-1][j+1] + gsp[i+1][j+1] + gsp[i+1][j] + gsp[i+1][j-1]
            if gsp[i][j] == 1:
                if neighbours < 2 or neighbours > 3:
                    temp_gsp[i][j] = 0
            else:
                if neighbours == 3:
                    temp_gsp[i][j] = 1
    img.set_data(temp_gsp)
    gsp[:] = temp_gsp[:]
    ax.set_xlabel(frame_number)
    return img

def read_from_file():
    with open("gamespace", "r") as gsp_file:
        initialise_space = []
        for x in [line.strip().split() for line in gsp_file.read().strip().split("\n")]:
            initialise_space.append([int(i) for i in list(x[0])])
        return initialise_space

if __name__ == "__main__":
    question = input("Read from file (f) or create random space (r) ? ")
    if question in "fF":
        gsp = np.array(read_from_file())
        rows = len(gsp)
        columns = len(gsp[0])
    elif question in "rR":
        rows = int(input("Enter rows "))
        columns = int(input("Enter columns "))
        gsp = np.array(random_grid(rows, columns))
    else:
        print("Invalid input")
        exit()
    
    figure, ax = plt.subplots()
    img = ax.imshow(gsp, cmap="gray")
    anime = FuncAnimation(figure, update_anime_func, fargs=(img, gsp, rows, columns,), frames=200, repeat=False, interval=100)
    plt.title("The Game of Life")
    plt.show()