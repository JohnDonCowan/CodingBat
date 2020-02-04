def without_end(str):
    """
    Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'
    :param str: a string of at least 2 chars
    :return: a string, str without the first and last char
    """
    return str[1:len(str) - 1]