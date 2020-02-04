def xyz_there(str):
    """
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
    :param str: a string
    :return: boolean, True if the string contains xyz without a period in front
    """
    for i in range(len(str) - 2):
        if i == 0 and str[0:3] == 'xyz':
            return True
        elif str[i - 1] != '.' and str[i:i + 3] == 'xyz':
            return True
    return False
