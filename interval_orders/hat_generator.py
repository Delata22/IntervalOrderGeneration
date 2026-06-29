from interval_orders.bin_utils import int_to_bin_array


def generate_hat(order):
    """
    Generate all binary arrays of length `order` that start and end with 1.

    :param order: The length of the binary arrays to generate. Must be >= 2.
    :return: Generator[List[int]] - Yields binary lists of length `order` where
                                    the first and last elements are 1.
    """
    for i in range((1 << (order - 1)) + 1, (1 << order), 2):
        yield int_to_bin_array(i)