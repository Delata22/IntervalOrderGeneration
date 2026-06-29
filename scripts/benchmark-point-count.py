from interval_orders.generator import generate_order
import time

# Benchmark: Generate all interval orders with `i` points and measure execution time for each.
for i in range(1, 20):

    start = time.time()
    count = 0
    for interval_order in generate_order(i):
        count += 1
    end = time.time()
    print(f"Order {i} - {count} - {end - start:.4f} seconds")
