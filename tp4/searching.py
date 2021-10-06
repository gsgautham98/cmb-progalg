from math import floor

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

A = [1, 8, 3, 7, 9, 2, 6, 5, 1]
print(sequential_search(8, A), binary_search(8, sorted(A)))