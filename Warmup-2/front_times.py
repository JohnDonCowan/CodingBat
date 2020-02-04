def front_times(str, n):
    """
    Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'

    :param str: a string
    :param n: a non-negative int
    :return: a string of the first three chars of str looped n times
    """
    result = ""
    if len(str) < 3:
        front = str
    else:
        front = str[:3]
    for i in range(n):
        result += front
    return result