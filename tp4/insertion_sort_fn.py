from time import time
from random import randint
import matplotlib.pyplot as plt

def insertion_sort(a):
    n = len(a)
    i = 2
    for i in range(n):
        x = a[i]
        j = i
        while j > 0 and a[j-1] > x:
            a[j] = a[j-1]
            j = j - 1
        a[j] = x
        i+=1
    return a

if __name__ == "__main__":
    A = [randint(1, 10000) for _ in range(1000)]
    start_time = time()
    A_sorted = insertion_sort(A)
    print(time() - start_time)
    print("Final array ", A_sorted)

# Time taken n=8: 4.291534423828125e-06
# Time taken n=16: 9.298324584960938e-06
# Time taken n=32: 3.0994415283203125e-05
# Time taken n=64: 9.751319885253906e-05
# Time taken n=128: 0.00037598609924316406
# Time taken n=256: 9.751319885253906e-05
# Time taken n=512: 9.751319885253906e-05
# Time taken n=1024: 9.751319885253906e-05
# Time taken n=2048: 9.751319885253906e-05