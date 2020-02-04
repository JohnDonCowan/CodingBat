def close_far(a, b, c):
    """
Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.

close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True
    :param a: int value
    :param b: int value
    :param c: int value
    :return: boolean, True if one of b or c is within 1 of a and one is at least 2 from the other two values
    """
    (abs(b - a) <= 1 and abs(c - b) >= 2 and abs(c - a) >= 2)