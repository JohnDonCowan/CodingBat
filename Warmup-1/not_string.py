def not_string(str):
    """
    Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'

    :param str: string
    :return: string str with "not" added to front unless "not" was already in front
    """
    if str[:3] == 'not':
        return str
    else:
        return 'not ' + str