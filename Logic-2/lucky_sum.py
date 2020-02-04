def lucky_sum(a, b, c):
    """
    Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.

lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1
    :param a: int value
    :param b: int value
    :param c: int value
    :return: sum of all values in the sequence a, b and c up until 13 is reached
    """
    sum = 0
    if a == 13:
        return sum
    sum += a
    if b == 13:
        return sum
    sum += b
    if c == 13:
        return sum
    return sum + c
