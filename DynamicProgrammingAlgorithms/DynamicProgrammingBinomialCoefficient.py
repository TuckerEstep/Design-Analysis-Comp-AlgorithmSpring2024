import random
import time

def binomial_coefficient(n, k):
    C = [[0 for x in range(k+1)] for x in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
    return C[n][k]

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
    num_tests = 21
    for _ in range(num_tests):
        n = random.randint(min_n, max_n)
        k = random.randint(min_k, min(n, max_k))
        avg_time, result = measure_runtime(n, k)
        import random
        import time


        def binomial_coefficient_dp(n, k):
            # Create a 2D array for storing intermediate results
            C = [[0 for x in range(k + 1)] for x in range(n + 1)]

            # Calculate Binomial Coefficient in bottom up manner
            for i in range(n + 1):
                for j in range(min(i, k) + 1):
                    # Base cases
                    if j == 0 or j == i:
                        C[i][j] = 1
                    else:
                        C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

            return C[n][k]


        def measure_runtime_dp(n, k, num_iterations=10):
            total_time = 0.0
            for _ in range(num_iterations):
                start_time = time.time()
                result = binomial_coefficient_dp(n, k)
                end_time = time.time()
                total_time += (end_time - start_time)
            return total_time / num_iterations, result


        if __name__ == '__main__':
            min_n, max_n = 200, 500
            min_k, max_k = 100, 350
            num_tests = 1

            for _ in range(num_tests):
                n = random.randint(min_n, max_n)
                k = random.randint(min_k, min(n, max_k))
                avg_time, result = measure_runtime_dp(n, k)
                print("n value:", n, "k value:", k, )
                print('Average runtime:', avg_time, 'seconds')
