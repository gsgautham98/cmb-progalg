import numpy as np

def read_file():
    with open("input", "r") as fhandle:
        space = []
        for s in [line.strip().split() for line in fhandle.read().strip().split("\n")]:
            space.append([int(i) for i in list(s[0])])
        return space

def transition1(neighbours, rule):          # Transition rule system/function 1
    return rule[neighbours]

def transition2(neighbours, rule, current):         # Transition rule system/function 2
    return rule[current][neighbours]

def gradient(size, tgt):            # Calculating gradient for directed dynamics 2D cellular autamaton
    gradspace = np.zeros(size, dtype=float)
    for i in range(size[0]):
        for j in range(size[1]):
            eudist = ((i - tgt[0]) ** 2 + (j - tgt[1]) ** 2) ** 0.5
            gradspace[i, j] = 1 / np.exp(0.8 * eudist - 1)
    return gradspace


# All cellular automata updaters #

def updater1(space, size, rule):
    tempspace = np.copy(space)
    for i in range(size):
        if i == 0:
            tempspace[i] = transition1(tempspace[i+1], rule)
        elif i == len(space) - 1:
            tempspace[i] = transition1(tempspace[i-1], rule)
        else:
            tempspace[i] = transition1(tempspace[i-1] + tempspace[i+1], rule)
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

def updater2_animated(frame_number, img, ax, space, size, rule):
    tempspace = np.copy(space)
    for i in range(1, size[0]-1):
        for j in range(1, size[1]-1):
            neighbours = space[i, j+1] + space[i, j-1] + space[i+1, j] + space[i-1, j] + space[i+1, j+1] + space[i-1, j-1] + space[i+1, j-1] + space[i-1, j+1]
            tempspace[i, j] = transition2(neighbours, rule, space[i, j])
    img.set_data(tempspace)
    space[:] = tempspace[:]
    ax.set_xlabel(frame_number)
    return img

def updater3(space, size, rule):
    tempspace = np.copy(space)
    for i in range(1, size[0]-1):
        for j in range(1, size[1]-1):
            neighbours = space[i, j+1] + space[i, j-1] + space[i+1, j] + space[i-1, j] + space[i+1, j+1] + space[i-1, j-1] + space[i+1, j-1] + space[i-1, j+1]
            tempspace[i, j] = transition1(neighbours, rule)
    space[:] = tempspace[:]
    return space

def updater3_animated(frame_number, img, ax, space, size, rule):
    tempspace = np.copy(space)
    for i in range(1, size[0]-1):
        for j in range(1, size[1]-1):
            neighbours = space[i, j+1] + space[i, j-1] + space[i+1, j] + space[i-1, j] + space[i+1, j+1] + space[i-1, j-1] + space[i+1, j-1] + space[i-1, j+1]
            tempspace[i, j] = transition1(neighbours, rule)
    img.set_data(tempspace)
    space[:] = tempspace[:]
    ax.set_xlabel("Frame " + str(frame_number) + ": " + str(100 * np.sum(space) / (size[0] * size[1])) + " percent filled")
    return img

def updater(frame_number, img, space, size, rule):
    tempspace = np.copy(space)
    for i in range(size[0]):
        for j in range(size[1]):
            try:
                neighbours = space[i, j+1] + space[i, j-1] + space[i+1, j] + space[i-1, j] + space[i+1, j+1] + space[i-1, j-1] + space[i+1, j-1] + space[i-1, j+1]
                tempspace[i, j] = transition2(neighbours, rule, space[i, j])
            except IndexError:
                if tempspace[i, j] == 1:
                    tempspace[i, j] = 0 if np.random.uniform() > 0.75 else 1
                else:
                    tempspace[i, j] = 1 if np.random.uniform() > 0.96 else 0
    img.set_data(tempspace)
    space[:] = tempspace[:] 
    return img