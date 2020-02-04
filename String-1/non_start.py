def non_start(a, b):
    """
    Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'
    :param a: a string of at least 1 char
    :param b: a string of at least 1 char
    :return: a string, the concatenation of a and b without their first chars
    """
    return a[1:] + b[1:]