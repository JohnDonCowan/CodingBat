def makes10(a,b):
    """
    Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True

    :param a: int value
    :param b: int value
    :return: boolean, True if a or b equal or sum to 10
    """
    return (a==10 or b==10 or (a+b)==10)