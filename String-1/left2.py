def left2(str):
    """
    Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

left2('Hello') → 'lloHe'
left2('java') → 'vaja'
left2('Hi') → 'Hi'
    :param str: a string of at least 2 chars
    :return: a string, str where the first 2 chars are moved to the end
    """
    return str[2:] + str[:2]