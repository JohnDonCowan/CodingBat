def string_bits(str):
    """
    Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
    :param str: a string
    :return: a string made up of every odd-numbered char in str
    """
    result = ""
    i = 0
    while i < len(str):
        result += str[i]
        i += 2
    return result