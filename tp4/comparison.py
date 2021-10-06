from heap_sort import heapify, heap_sort_fn, sift_down
from insertion_sort_fn import insertion_sort
from random import randint
from time import time
import matplotlib.pyplot as plt

inputs = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
time_ins = []
time_heap = []
for i in inputs:
    A = [randint(1, 10000) for _ in range(i)]
    start_ins = time()
    result = insertion_sort(A)
    time_ins.append(time() - start_ins)
    start_heap = time()
    result = heap_sort_fn(A)
    time_heap.append(time() - start_heap)

    print(time_ins, time_heap)

print(time_ins, time_heap)
plt.plot(inputs, time_ins, "blue")
plt.plot(inputs, time_heap, "red")
plt.show()