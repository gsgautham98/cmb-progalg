def insertion_sort_fn(a):
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