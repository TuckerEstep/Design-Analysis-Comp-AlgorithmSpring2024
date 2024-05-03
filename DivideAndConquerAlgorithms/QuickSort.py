import random
import time
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot= arr[random.randint(0, len(arr)-1)]
    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]

    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)

def avg_time_to_sort( arr, num_iterations=10):
    total_time = 0.0
    for _ in range(num_iterations):
        start_time = time.time()
        sorted_arr = quick_sort(arr.copy())
        end_time = time.time()
        total_time += (end_time - start_time)
    return total_time / num_iterations

if __name__ == '__main__':
    data_size = 200000
    test_data = [random.randint(1, 1000) for _ in range(data_size)]

    avg_time = avg_time_to_sort(test_data)
    print('Average time take for quick sort:', avg_time, 'seconds')