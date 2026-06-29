import math

from interval_orders.generator import generate_order, complete_proto
import time

from interval_orders.hat_generator import generate_hat
from interval_orders.proto_generator import get_good_truc, generate_proto

for i in range(9, 10):
    start = time.time()
    count_proto = 0 if i != 1 else 1
    for hat in generate_hat(i):
        blank = get_good_truc(hat, i)
        for proto, max_x, max_y, left in generate_proto(i, blank, 0, 1, hat.copy(), hat.copy(), [math.inf]):
            count_proto += 1
            print(count_proto)
    end = time.time()
    print(f"First line of size {i} - proto: {count_proto} - {end - start:.4f} seconds")
