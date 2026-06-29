def int_to_bin_array(n):
    """
    Convert an integer to a list of binary digits.

    :param n: int - A non-negative integer to be converted to binary.
    :return: List[int] - A list of 0s and 1s representing the binary form of `n`,
                         with the most significant bit first.
    """
    return [int(bit) for bit in bin(n)[2:]]
