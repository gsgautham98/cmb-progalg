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
    if len(sequence) < 1:
        return False
    elif item == sequence[midpoint]:
        return True
    elif item > sequence[midpoint]:
        return binary_search(item, sequence[midpoint+1:])
    elif item < sequence[midpoint]:
        return binary_search(item, sequence[:midpoint])
    else:
        return False

inputs = (8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536)
time_seqsrch = []
time_binsrch = []

for i in inputs:
    A = sorted([randint(1, i) for _ in range(i)])
    for _ in range(1000):
        query = randint(1, i)
        tempseq = []
        start_seqsrch = time()
        sequential_search(query, A)
        tempseq.append(time() - start_seqsrch)
        tempbin = []
        start_binsrch = time()
        binary_search(query, A)
        tempbin.append(time() - start_binsrch)
    time_seqsrch.append(sum(tempseq) / len(tempseq))
    time_binsrch.append(sum(tempbin) / len(tempbin))

plot_seqsrch = plt.plot(inputs, time_seqsrch, "blue", label="Sequential search")
plot_binsrch = plt.plot(inputs, time_binsrch, "red", label="Binary search")
plt.title("Comparison between time complexities of searching methods")
plt.legend()
plt.show()