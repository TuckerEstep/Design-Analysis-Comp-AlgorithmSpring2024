import random
import time

def generate_item_sizes(num_items, min_size=1, max_size=100):
    return [random.randint(min_size, max_size) for _ in range(num_items)]

def first_fit(item_sizes, bin_capacity):
    sorted_item_sizes = sorted(item_sizes, reverse=True)
    bins = []

    for item in sorted_item_sizes:
        placed = False
        for i in range(len(bins)):
            if bins[i] + item <= bin_capacity:
                bins[i] += item
                placed = True
                break
        if not placed:
            bins.append(item)
    return len(bins)

def time_to_compute(num_items, bin_capacity):
    item_sizes = generate_item_sizes(num_items)
    start_time = time.time()
    num_bins = first_fit(item_sizes, bin_capacity)
    end_time = time.time()
    total_time = end_time - start_time
    return num_bins, total_time

if __name__ == '__main__':
    num_items = 50000
    bin_capacity = 50000
    num_bins, exec_time = time_to_compute(num_items, bin_capacity)

    print(f'This algorithm used {num_bins} bins, and took {exec_time:.6f} seconds to solve')
