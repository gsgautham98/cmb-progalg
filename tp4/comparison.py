from heap_sort import heap_sort_fn
from insertion_sort import insertion_sort_fn
from random import randint
from time import time
import matplotlib.pyplot as plt

inputs = (8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096)
time_ins = []
time_heap = []
time_def = []

for i in inputs:
    A = [randint(1, 10000) for _ in range(i)]
    start_ins = time()
    insertion_sort_fn(A)
    time_ins.append(time() - start_ins)
    start_heap = time()
    heap_sort_fn(A)
    time_heap.append(time() - start_heap)
    start_def = time()
    A.sort()
    time_def.append(time() - start_def)

plot_ins = plt.plot(inputs, time_ins, "blue", label="Insertion sort")
plot_heap = plt.plot(inputs, time_heap, "red", label="Heapsort")
plot_def = plt.plot(inputs, time_def, "black", label="Default sort")
plt.title("Comparison between time complexities of sorting methods")
plt.xlabel("Input size")
plt.ylabel("Average execution time")
plt.legend()
plt.show()