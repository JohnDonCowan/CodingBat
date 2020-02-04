def first_two(str):
    """
    Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".

first_two('Hello') → 'He'
first_two('abcdefg') → 'ab'
first_two('ab') → 'ab'
    :param str: a string
    :return: a string made of the first two chars of str, or the whole of str if its length is less than 2 chars
    """
    if len(str) < 2:
        return str
    else:
        return str[:2]
