def front3(str):
    """
    Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.

front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
    :param str: string
    :return: string str's first 3 chars (or the entire str if it contains less than 3 chars) repeated three times
    """
    if len(str) < 3:
        front = str
    else:
        front = str[:3]
    return front + front + front