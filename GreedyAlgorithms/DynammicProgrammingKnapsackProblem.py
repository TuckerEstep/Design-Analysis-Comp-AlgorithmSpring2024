import random
import time

def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    result = dp[n][capacity]
    return result

def generate_items(num_items, max_weight, max_value):
    values = [random.randint(1, max_value) for _ in range(num_items)]
    weights = [random.randint(1, max_weight) for _ in range(num_items)]
    return values, weights

def main():
    num_items = 500
    max_weight = 100
    max_value = 100
    capacity = 50

    values, weights = generate_items(num_items, max_weight, max_value)

    start_time = time.time()
    max_value = knapsack(values, weights, capacity)
    end_time = time.time()

    print("Our knapsack has a capacity of 50 with 500 potential items to put in it all with a max weight and max value of 100.")
    print("Max value in our knapsack is: ", max_value)
    print("It took:", end_time - start_time, "seconds to compute.")

if __name__ == "__main__":
    main()