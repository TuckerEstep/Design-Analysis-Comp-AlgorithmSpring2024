import random
import time

def generate_item_sizes(num_items, min_size=1, max_size=100):
    return [random.randint(min_size, max_size) for _ in range(num_items)]

def next_fit(item_sizes, bin_capacity):
    sorted_item_sizes = sorted(item_sizes, reverse=True)
    bins = []
    current_bin_capacity = 0

    for item in sorted_item_sizes:
        if current_bin_capacity + item <= bin_capacity:
            current_bin_capacity += item
        else:
            bins.append(item)
            current_bin_capacity = item
    return len(bins)

def measure_time_and_compute(num_items, bin_capacity):
    item_sizes = generate_item_sizes(num_items)
    start_time = time.time()
    num_bins = next_fit(item_sizes, bin_capacity)
    end_time = time.time()
    time_taken = end_time - start_time

    return num_bins, time_taken

if __name__ == '__main__':
    num_items = 100000
    bin_capacity = 50000

    num_bins, exec_time = measure_time_and_compute(num_items, bin_capacity)

    print(f'This algorithm used {num_bins} bins, and took {exec_time:.6f} seconds to solve')