import random
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr


    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)
def merge(left, right):
    sorted_arr = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_arr.append(left[left_index])
            left_index += 1
        else:
            sorted_arr.append(right[right_index])
            right_index += 1

    sorted_arr.extend(left[left_index:])
    sorted_arr.extend(right[right_index:])

    return sorted_arr

def time_to_sort(arr, num_iterations=10):
    total_time = 0.0
    for _ in range(num_iterations):
        start_time = time.time()
        sorted_arr = merge_sort(arr.copy())
        end_time = time.time()
        total_time += (end_time - start_time)
    return total_time / num_iterations


if __name__ == '__main__':
    data_size = 200000
    test_data = [random.randint(1, 1000) for _ in range(data_size)]

    avg_time = time_to_sort(test_data)
    print('Average time taken for Merge Sort:', avg_time, 'seconds')