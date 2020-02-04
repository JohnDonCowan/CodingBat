def diff21(n):
    """
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
    :param n: int value
    :return: int, the absolute difference between n and 21, or double if n is greater than 21
    """
    if n > 21:
        return 2 * (n - 21)
    else:
        return 21 - n