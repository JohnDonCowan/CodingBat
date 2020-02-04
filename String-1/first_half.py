def first_half(str):
    """
    Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'
    :param str: a string of even length
    :return: a string, the first half of str
    """
    return str[:len(str) / 2]