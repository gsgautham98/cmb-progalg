import numpy as np

def read_file():
    with open("input", "r") as fhandle:
        space = []
        for s in [line.strip().split() for line in fhandle.read().strip().split("\n")]:
            space.append([int(i) for i in list(s[0])])
        return space

def transition1(neighbours, rule):
    return rule[neighbours]

def transition2(neighbours, rule, current):
    return rule[current][neighbours]

def gradient(size, tgt):
    gradspace = np.zeros(size, dtype=float)
    for i in range(size[0]):
        for j in range(size[1]):
            eudist = ((i - tgt[0]) ** 2 + (j - tgt[1]) ** 2) ** 0.5
            gradspace[i, j] = -eudist
    gradspace[tgt[0]:tgt[0]+2, tgt[1]:tgt[1]+2] = np.array([[100, 100], [100, 100]])
    return gradspace

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
    for i in range(1, size[0]-1):
        for j in range(1, size[1]-1):
            neighbours = space[i, j+1] + space[i, j-1] + space[i+1, j] + space[i-1, j] + space[i+1, j+1] + space[i-1, j-1] + space[i+1, j-1] + space[i-1, j+1]
            tempspace[i, j] = transition2(neighbours, rule, space[i, j])
    space[:] = tempspace[:]
    return space

def updater2i(frame_number, img, ax, space, size, rule):
    tempspace = np.copy(space)
    for i in range(1, size[0]-1):
        for j in range(1, size[1]-1):
            neighbours = space[i, j+1] + space[i, j-1] + space[i+1, j] + space[i-1, j] + space[i+1, j+1] + space[i-1, j-1] + space[i+1, j-1] + space[i-1, j+1]
            tempspace[i, j] = transition2(neighbours, rule, space[i, j])
    img.set_data(tempspace)
    space[:] = tempspace[:]
    ax.set_xlabel(frame_number)
    return img