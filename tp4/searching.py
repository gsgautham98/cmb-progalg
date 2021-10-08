from math import floor
from random import randint
from time import time
import matplotlib.pyplot as plt

def sequential_search(item, sequence):
    item_found = False
    for i in range(len(sequence)):
        if item == sequence[i]:
            item_found = True
            break
    return item_found

def binary_search(item, sequence):
    midpoint = floor(len(sequence) / 2)
    if item > sequence[midpoint] and len(sequence) > 1:
        return binary_search(item, sequence[midpoint+1:])
    elif item < sequence[midpoint] and len(sequence) > 1:
        return binary_search(item, sequence[:midpoint])
    elif item == sequence[midpoint]:
        return True
    else:
        return False

inputs = (8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096)
time_seqsrch = []
time_binsrch = []

for i in inputs:
    A = [randint(1, 10000) for _ in range(i)]
    start_seqsrch = time()
    sequential_search(81, A)
    time_seqsrch.append(time() - start_seqsrch)
    start_binsrch = time()
    binary_search(81, A)
    time_binsrch.append(time() - start_binsrch)

plot_seqsrch = plt.plot(inputs, time_seqsrch, "blue", label="Sequential search")
plot_binsrch = plt.plot(inputs, time_binsrch, "red", label="Binary search")
plt.title("Comparison between time complexities of searching methods")
plt.legend()
plt.show()