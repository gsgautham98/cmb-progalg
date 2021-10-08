from math import floor

def swap(a, x, y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp
    return a

def sift_down(a, first, last):
    root = first
    while (2 * root) + 1 <= last:
        child = 2 * root + 1
        s = root
        if a[s] < a[child]:
            s = child
        if child + 1 <= last and a[s] < a[child+1]:
            s = child + 1
        if s == root:
            return a
        else:
            swap(a, root, s)
            root = s
    return a

def heapify(a, last):
    for i in range(floor((last - 1) / 2), -1, -1):
        a = sift_down(a, i, len(a) - 1)
    return a

def heap_sort_fn(a):
    a = heapify(a, len(a) - 1)
    last = len(a) - 1
    while last > 0:
        swap(a, last, 0)
        last-=1
        a = sift_down(a, 0, last)
    return a