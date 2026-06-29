def get_good_truc(first_line, order):
    """
    Build a binary triangle from a given top row, where all subsequent rows are filled with zeros.

    FIXME: We clearly need to find a real name for this function

    :param first_line: List[int] - The top row of the triangle (list of 0s and 1s),
                                   must have length equal to `order`.
    :param order: int - The total number of rows in the triangle. Must match the length of `first_line`.
    :return: List[List[int]] - A triangle represented as a list of lists, where the first row is `first_line`
                               and each subsequent row contains only zeros with one less element.
    """
    result = [first_line]
    for i in range(order - 1, 0, -1):
        result.append([0] * i)
    return result


def generate_proto(order, curr, curr_x, curr_y, diag, cols, point_left):
    """
    Recursively generate all valid proto-matrices for a given order (size of the first line),
    subject to diagonal and column constraints, using backtracking.

    :param order: int - The size of the proto-matrix (order x order).
    :param curr: List[List[int]] - The current state of the proto-matrix being built.
    :param curr_x: int - The current x-position (column index) in the matrix.
    :param curr_y: int - The current y-position (row index) in the matrix.
    :param diag: List[int] - A list tracking the number of points on each diagonal.
                             Length should be `order`.
    :param cols: List[int] - A list tracking the number of points in each column.
                             Length should be `order`.
    :param point_left: List[int] - A one-element list containing the number of points
                                   still left to place. Used as a mutable integer reference.

    :yield: Tuple[List[List[int]], int, int, List[int]] - Yields valid configurations of the proto-matrix
            along with the final positions and remaining points.
    """
    if all(diag) and all(cols):
        yield curr, curr_x, curr_y, point_left
        return

    if curr_y == order - 1:
        return

    if point_left[0] < max(diag.count(0), cols.count(0)):
        return

    if curr_x == 0 and diag[curr_y] == 0:
        curr[curr_y][curr_x] = 1
        diag[curr_y] += 1
        point_left[0] -= 1

        yield from generate_proto(order, curr, curr_x + 1, curr_y, diag, cols, point_left)

        diag[curr_y] -= 1
        curr[curr_y][curr_x] = 0
        point_left[0] += 1
        return

    if curr_x == order - 1 - curr_y and cols[curr_x] == 0:
        curr[curr_y][curr_x] = 1
        cols[curr_x] += 1
        point_left[0] -= 1

        yield from generate_proto(order, curr, 0, curr_y + 1, diag, cols, point_left)

        cols[curr_x] -= 1
        curr[curr_y][curr_x] = 0
        point_left[0] += 1
        return

    new_x = 0 if curr_x == order - 1 - curr_y else curr_x + 1
    new_y = curr_y if new_x != 0 else curr_y + 1

    yield from generate_proto(order, curr, new_x, new_y, diag, cols, point_left)

    curr[curr_y][curr_x] = 1
    diag[curr_y + curr_x] += 1
    cols[curr_x] += 1
    point_left[0] -= 1

    yield from generate_proto(order, curr, new_x, new_y, diag, cols, point_left)

    diag[curr_y + curr_x] -= 1
    cols[curr_x] -= 1
    curr[curr_y][curr_x] = 0
    point_left[0] += 1
