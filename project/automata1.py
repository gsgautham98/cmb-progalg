import numpy as np

def transition(rule, neighbours):
    return rule[neighbours]

def updater(space, size, rule):
    tempspace = np.copy(space)
    for i in range(size):
        if i == 0:
            tempspace[i] = transition(rule, tempspace[i+1])
        elif i == len(space) - 1:
            tempspace[i] = transition(rule, tempspace[i-1])
        else:
            tempspace[i] = transition(rule, tempspace[i-1] + tempspace[i+1])
    space[:] = tempspace[:]
    return space