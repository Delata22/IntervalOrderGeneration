from functools import lru_cache
import time

def can_generate_missing(n, curr_max, seens):
    count = 0
    for i in range(3, curr_max):
        if seens[i] == 0:
            count += 1
    return n * 2 >= count

def is_interval_order(passed, curr_max, seens):
    for i in range(3, curr_max - 1):
        if seens[i] == 0:
            return 0
    if (curr_max - 1, curr_max) not in passed:
        return 0
    return 1


@lru_cache(maxsize=None)
def generate_next(curr, curr_max, order):
    result = []
    for size in range(max(3, curr[1] - curr[0]), curr_max + order, 2):
        for first in range(1 if size != curr[1] - curr[0] else curr[0], curr_max + order // 2 - size, 2):
            result.append((first, first + size))

    if curr[1] - curr[0] == 1:
        for x in range(curr[0], curr_max + order * 2 - 2, 2):
            result.append((x, x + 1))
    print(f"Generate next : {curr} - {curr_max} - {order} - {result}")
    return result


# @lru_cache(maxsize=None)
def build_order(n, last, curr_max, passed, result, seens):
    passed.append(last)
    seens[last[0]] += 1
    seens[last[1]] += 1

    if n == 1:
        if is_interval_order(passed, curr_max, seens):
            result.append(passed.copy())
        seens[last[0]] -= 1
        seens[last[1]] -= 1
        passed.pop()
        return

    if curr_max - 4 <= n * 2 or can_generate_missing(n, curr_max, seens):
        for x in generate_next(last, curr_max, n):
            build_order(n - 1, x, max(x[1], curr_max), passed, result, seens)

    seens[last[0]] -= 1
    seens[last[1]] -= 1
    passed.pop()


def generate_count():
    for i in range(1, 100):
        result = []
        passed = []
        start = time.time()
        build_order(i, (1, 2), 2, passed, result, [0 for _ in range(i * i * 2 + 1)])
        end = time.time()
        print(f"Order {i} is of size {len(result)} -  {end - start:.4f} seconds")

#print(generate_next((7, 8), 8, 4))
#save_order(7)
#generate_count()
result  = []
build_order(4, (1, 2), 2, [], result, [0 for _ in range(4 * 4 * 2 + 1)])
print(result)