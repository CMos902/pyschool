
def raise_power(base_num: int, exponent: int):
    """
    Calculate the result of raising a base number to an exponent using recursion.

    :param base_num: The base number.
    :param exponent: The exponent (must be >= 0).

    :return: The result of raising a base number to an exponent.
    """
    result = 1
    if exponent > 0:
        result = raise_power(base_num, exponent // 2)
        result *= result
        if exponent % 2 != 0:
            result *= base_num
    return result

