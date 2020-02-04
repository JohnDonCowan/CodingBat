def sum_double(a, b):
    """
    Given two int values, return their sum. Unless the two values are the same, then return double their sum.

sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8

    :param a: int value
    :param b: int value
    :return: the integer sum of a and b, or double the sum if a and b are equal
    """
    if a == b:
        return 2 * (a + b)
    else:
        return a + b