from interval_orders.hat_generator import generate_hat
from interval_orders.proto_generator import get_good_truc, generate_proto


def complete_proto(proto, max_x, max_y, curr_x, curr_y, point_left, order):
    """
    Complete a proto-matrix by placing the remaining points (incrementing values) in valid lower-triangular positions,
    while respecting modification rules based on position relative to the proto's initial extent.


       :param proto: List[List[int]] - A proto-matrix partially filled, which already satisfies the required
                                       diagonal and column constraints.
       :param max_x: int - The furthest column index reached in the initial proto-matrix (used to mark original extent).
       :param max_y: int - The furthest row index reached in the initial proto-matrix.
       :param curr_x: int - The current column index being considered for addition.
       :param curr_y: int - The current row index being considered for addition.
       :param point_left: List[int] - A one-element mutable list representing how many points remain to place.
       :param order: int - The size (height) of the triangular matrix.

       :yield: List[List[int]] - Fully completed matrices where all remaining points have been placed,
                                 possibly incrementing cell values (i.e., values > 1 are allowed).

        Rules:
       - The matrix is lower-triangular: row i has (order - i) columns.
       - If the current position is **before the max proto point** (i.e., `curr_y < max_y`
         or `curr_y == max_y and curr_x < max_x`):
           - You may **increment the cell** **only if its value ≥ 1**.
           - You must **skip 0s** in this region — they cannot be modified.
       - If the current position is **at or after the max point**:
           - You may increment **any cell**, including those with 0.
       - When all remaining points are placed (`point_left[0] == 0`), the matrix is yielded.
       """
    if point_left[0] <= 0:
        yield proto
        return

    if curr_y >= order:
        return

    if proto[curr_y][curr_x] != 0 or curr_y > max_y or (curr_y >= max_y and curr_x >= max_x):
        proto[curr_y][curr_x] += 1
        point_left[0] -= 1
        yield from complete_proto(proto, max_x, max_y, curr_x, curr_y, point_left, order)

        proto[curr_y][curr_x] -= 1
        point_left[0] += 1

    new_x = 0 if curr_x == order - 1 - curr_y else curr_x + 1
    new_y = curr_y if new_x != 0 else curr_y + 1
    yield from complete_proto(proto, max_x, max_y, new_x, new_y, point_left, order)


def generate_order(order):
    """
    Generate all valid interval-order matrices for a given number of points.

    :param order: int - The number of points to place in the final structure.
    :return: Generator[List[List[int]]] - Yields fully completed proto-matrices representing valid interval orders.

    The generation process includes:
        - Iterating over all binary hat vectors of size from 1 to `order`, where each hat starts and ends with 1.
        - Using each hat to create an initial blank proto-matrix with `get_good_truc`.
        - Filling diagonals and columns with points using `generate_proto`.
        - Completing the matrix by placing remaining points using `complete_proto`.

    Special Case:
        If order == 1, a trivial order ([[1]]) is directly yielded.
    """
    for i in range(1, order + 1):
        for hat in generate_hat(i):
            blank = get_good_truc(hat, i)
            for proto, max_x, max_y, left in generate_proto(i, blank, 0, 1, hat.copy(), hat.copy(), [order - sum(hat)]):
                yield from complete_proto(proto, max_x, max_y, 0, 0, left, i)
        if i == 1:
            yield [[order]]
            continue
