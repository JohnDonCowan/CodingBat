def double_char(str):
    """
    Given a string, return a string where for every char in the original, there are two chars.

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'
    :param str: a string
    :return: a string containing two of every char in str
    """
    result = ""
    for i in range(len(str)):
        result += str[i] + str[i]
    return result