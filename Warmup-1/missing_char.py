def missing_char(str, n):
    """
    Given a non-empty string and an int n, return a new string where the char at index n has been removed.
    The value of n will be a valid index of a char in the original string
    (i.e. n will be in the range 0..len(str)-1 inclusive).

    missing_char('kitten', 1) → 'ktten'
    missing_char('kitten', 0) → 'itten'
    missing_char('kitten', 4) → 'kittn'

    :param str: A non-empty string
    :param n: A positive integer that is a valid index of a character in the original string
    :return: The string 'str' with the character at position 'n' removed.
    """
    return str[:n] + str[n+1:]