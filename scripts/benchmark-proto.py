import math

from interval_orders.generator import generate_order, complete_proto
import time

from interval_orders.hat_generator import generate_hat
from interval_orders.proto_generator import get_good_truc, generate_proto

for i in range(1, 20):
    start = time.time()
    count_proto = 0 if i != 1 else 1
    for t in range(1,i+1):
        for hat in generate_hat(t):
            blank = get_good_truc(hat, i)
            for proto, max_x, max_y, left in generate_proto(t, blank, 0, 1, hat.copy(), hat.copy(), [i - sum(blank[0])]):
                if sum([sum(p) for p in proto]) == i:
                    # print(f"{i} - {proto}")
                    count_proto += 1
    end = time.time()
    print(f"Number of proto with {i} events : {count_proto} - {end - start:.4f} seconds")
