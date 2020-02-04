def pos_neg(a, b, negative):
    """
    Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.

pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True

    :param a: int value
    :param b: int value
    :param negative: boolean, determinant if both values are negative
    :return: boolean, True if one is negative and one is positive while negative is False, or both are negative while negative is True
    """
    if negative == False:
        return (a * b < 0)
    elif negative == True:
        return (a < 0 and b < 0)