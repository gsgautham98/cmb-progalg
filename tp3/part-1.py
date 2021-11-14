import random, sys
import matplotlib.pyplot as plt

# Task 1
def gen_rand(n):
    return [random.random() for _ in range(n)]

# Task 2
def three_plots(N, R):
    plt.figure(1, figsize=(10, 15))
    plt.subplot(311)
    plt.plot(N, R, color='blue')
    plt.subplot(312)
    plt.plot(R[0:-1], R[1:], color='black')
    plt.subplot(313)
    plt.hist(R)
    plt.show()

# Task 3
if __name__ == "__main__":
    n = int(sys.argv[1])
    sequence = gen_rand(n)
    three_plots(range(n), sequence)