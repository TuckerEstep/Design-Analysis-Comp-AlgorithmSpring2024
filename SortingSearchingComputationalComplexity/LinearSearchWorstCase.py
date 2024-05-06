import random
import time

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def time_to_compute(arr, target, num_iterations=10):
    total_time = 0.0
    for i in range(num_iterations):
        start_time = time.time()
        result = linear_search(arr, target)
        end_time = time.time()
        total_time += (end_time - start_time)
    return total_time / num_iterations

def worse_case_dataset(size, target_position):
    dataset = list(range(1, size))
    dataset.append(target_position)
    return dataset

if __name__ == '__main__':
    data_size = 5000000
    target_value = data_size - 1
    worst_case_data = worse_case_dataset(data_size, target_value)

    average_time = time_to_compute(worst_case_data, target_value)
    print('Average time taken for Linear Search with worst-case time complexity:', average_time)