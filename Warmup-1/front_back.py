def front_back(str):
    """
Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'

    :param str: a string
    :return: string str where the first and last letters have been exchanged
    """
    length = len(str)
    if length <= 1:
        return str
    else:
        return str[length - 1] + str[1:-1] + str[0]