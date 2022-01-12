import numpy as np

def read_file():
    with open("input", "r") as fhandle:
        space = []
        for s in [line.strip().split() for line in fhandle.read().strip().split("\n")]:
            space.append([int(i) for i in list(s[0])])
        return space

def transition1(rule, neighbours):
    return rule[neighbours]

def transition2(neighbours, rule, current):
    return rule[current][neighbours]

def gradient(s, r, c, t):
    g = np.zeros((len(s), len(s[0])), dtype=float)
    for i in range(r):
        for j in range(c):
            ed = ((i - t[0]) ** 2 + (j - t[1]) ** 2) ** 0.5
            g[i, j] = 1 / (ed + 0.15)
    return g

def updater1(space, size, rule):
    tempspace = np.copy(space)
    for i in range(size):
        if i == 0:
            tempspace[i] = transition1(rule, tempspace[i+1])
        elif i == len(space) - 1:
            tempspace[i] = transition1(rule, tempspace[i-1])
        else:
            tempspace[i] = transition1(rule, tempspace[i-1] + tempspace[i+1])
    space[:] = tempspace[:]
    return space

def updater2(space, size, rule):
    tempspace = np.copy(space)
    for i in range(2, size[0]-2):
        for j in range(2, size[1]-2):
            neighbours = space[i, j+1] + space[i, j-1] + space[i+1, j] + space[i-1, j] + space[i+1, j+1] + space[i-1, j-1] + space[i+1, j-1] + space[i-1, j+1]
            tempspace[i, j] = transition2(neighbours, rule, space[i, j])
    space[:] = tempspace[:] 
    return space

def updater2a(frame_number, img, space, N, rule):
    tempspace = np.copy(space)
    for i in range(2, N-2):
        for j in range(2, N-2):
            neighbours = space[i, j+1] + space[i, j-1] + space[i+1, j] + space[i-1, j] + space[i+1, j+1] + space[i-1, j-1] + space[i+1, j-1] + space[i-1, j+1]
            tempspace[i, j] = transition1(neighbours, rule) if neighbours != 0 else 0
    img.set_data(tempspace)
    space[:] = tempspace[:] 
    # ax.set_xlabel(frame_number)
    return img