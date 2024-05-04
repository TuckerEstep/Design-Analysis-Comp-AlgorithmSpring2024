import random
import time
def knapsack(values, weights, capacity):
    n = len(values)
    items = list(zip(values, weights))

    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_weight = 0
    total_value = 0

    for value, weight in items:
        if total_weight + weight <= capacity:
            total_value += value
            total_weight += weight
        else:
            break
    return total_value

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