from interval_orders.generator import generate_order
import time
import matplotlib.pyplot as plt

# OEIS A137251
i = 10
start = time.time()
count = [0 for _ in range(i + 1)]
for interval_order in generate_order(i):
    count[len(interval_order)] += 1
end = time.time()

print(f"Number of points {i} : {sum(count)}")
for j in range(len(count)):
    print(f"Size {j} : {count[j]}")

sizes = list(range(len(count)))
plt.figure(figsize=(8, 5))
plt.plot(sizes, count, marker='o', linestyle='-', color='teal')
plt.title(f"Distribution of Interval Order Sizes (Total Points = {i})")
plt.xlabel("Size (number of rows)")
plt.ylabel("Count")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
for total_points, count in simulated_counts.items():
    sizes = list(range(len(count)))
    plt.plot(sizes, count, marker='o', label=f'{total_points} points')

plt.yscale('log')  # Log scale for Y-axis
plt.title("Distribution of Interval Order Sizes (Log Scale Y-Axis)")
plt.xlabel("Size (number of rows)")
plt.ylabel("Count (log scale)")
plt.legend(title="Total Points", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, which="both", linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()