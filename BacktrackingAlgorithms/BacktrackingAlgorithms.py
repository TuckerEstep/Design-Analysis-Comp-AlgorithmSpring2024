import random
import time
def knapsack(values, weights, capacity):
    n = len(values)
    max_value = [0]

    def backtrack(index, current_weight, current_value):
        if index == n or current_weight == 0:
            max_value[0] = max(max_value[0], current_value)
            return

        if current_weight - weights[index] >= 0:
            backtrack(index + 1, current_weight - weights[index], current_value + values[index])

        backtrack(index + 1, current_weight, current_value)

    backtrack(0, capacity, 0)
    return max_value[0]

def generate_items(num_items, max_weight, max_value):
    values = [random.randint(1, max_value) for _ in range(num_items)]
    weights = [random.randint(1, max_weight) for _ in range(num_items)]
    return values, weights

def main():
    num_items = 150
    max_weight = 100
    max_value = 100
    capacity = 50

    values, weights = generate_items(num_items, max_weight, max_value)

    start_time = time.time()
    max_value = knapsack(values, weights, capacity)
    end_time = time.time()

    print("Our knapsack has a capacity of 50 with 150 potential items to put in it all with a max weight and max value of 100.")
    print("Max value in our knapsack is: ", max_value)
    print("It took:", end_time - start_time, "seconds to compute.")

if __name__ == "__main__":
    main()