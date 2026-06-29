from functools import lru_cache


@lru_cache(maxsize=None)
def generate_next(curr, curr_max):
    result = []
    for size in range(curr[1] - curr[0], curr_max, 2):
        if size == 1:
            result.append((curr_max + 1, curr_max + 2))
        for first in range(1 if size != curr[1] - curr[0] else curr[0], curr_max - size + 1, 2):
            result.append((first, first + size))

    return result


@lru_cache(maxsize=None)
def build_order(n, last, curr_max):
    if n == 1:
        return [[last]]
    result = []
    for x in generate_next(last, curr_max):
        next_order = build_order(n - 1, x, x[1] if x[1] > curr_max else curr_max)
        for next in next_order:
            result.append([last] + next)
    return result


def generate_count():
    for i in range(1, 100):
        order = build_order(i, (1, 2), 2)
        print(f"Order {i} is of size {len(order)}")


generate_count()
