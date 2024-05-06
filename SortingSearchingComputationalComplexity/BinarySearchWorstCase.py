import random
import time

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def generate_sorted_dataset(size):
    return list(range(size))

def time_to_compute(data_size, num_iterations=10):
    total_time = 0.0

    for _ in range(num_iterations):
        dataset = generate_sorted_dataset(data_size)
        target_value = data_size + 1
        start_time = time.perf_counter()
        result = binary_search(dataset, target_value)
        end_time = time.perf_counter()
        total_time += (end_time - start_time)
    return total_time / num_iterations

if __name__ == '__main__':
    data_size = 5000000
    num_iterations = 10

    average_time = time_to_compute(data_size, num_iterations)

    print('Average time taken for Binary Search with worst-case time complexity:', average_time)
