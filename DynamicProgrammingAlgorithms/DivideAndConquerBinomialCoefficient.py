import random
import time

def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n -1, k)

def measure_runtime(n, k, num_iterations=10):
    total_time = 0.0
    for _ in range(num_iterations):
        start_time = time.time()
        result = binomial_coefficient(n, k)
        end_time = time.time()
        total_time += (end_time - start_time)
    return total_time / num_iterations, result


if __name__ == '__main__':
    min_n, max_n = 10, 30
    min_k, max_k = 5, 20
    num_tests = 1

    for _ in range(num_tests):
        n = random.randint(min_n, max_n)
        k = random.randint(min_k, min(n, max_k))
        avg_time, result = measure_runtime(n, k)
        print("n value:", n, "k value:", k,)
        print('Average runtime:', avg_time, 'seconds')
