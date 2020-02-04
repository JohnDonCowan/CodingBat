def no_teen_sum(a, b, c):
    """
    Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().

no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3
    :param a: int value
    :param b: int value
    :param c: int value
    :return: int value, the sum of non-teen values of a, b and c
    """
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    """
    Takes in an int value and returns that value fixed for the teen rule: if any of the values is in the range 13..19 inclusive, then that value counts as 0, except 15 and 16 do not count as a teens.
    :param n: an int
    :return: int value, 0 if n is a teen, n otherwise
    """
    if (n >= 13 and n < 15) or (n > 16 and n <= 19):
        return 0
    else:
        return n