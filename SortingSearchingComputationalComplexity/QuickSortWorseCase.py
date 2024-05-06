import random
import time
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_idx = partition(arr, low, high)
            stack.append((low, pivot_idx - 1))
            stack.append((pivot_idx + 1, high))
    return arr


def partition(arr, low, high):
    mid = (low + high) // 2
    pivot_idx = mid

    if arr[low] < arr[mid]:
        if arr[mid] < arr[high]:
            pivot_idx = mid
        elif arr[low] < arr[high]:
            pivot_idx = high

    elif arr[low] < arr[high]:
        pivot_idx = low

    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def avg_time_to_sort(arr, num_iterations=10):
    total_time = 0.0
    for _ in range(num_iterations):
        start_time = time.time()
        sorted_arr = quick_sort(arr.copy())
        end_time = time.time()
        total_time += (end_time - start_time)
    return total_time / num_iterations

def generate_worst_case_dataset(size):
    return list(range(1, size + 1))

if __name__ == '__main__':
    data_size = 200000
    worst_case_data = generate_worst_case_dataset(data_size)
    avg_time = avg_time_to_sort(worst_case_data)
    print('Average time take for quick sort with worst-case scenario time complexity:', avg_time, 'seconds')
