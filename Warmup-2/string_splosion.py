def string_splosion(str):
    """
    Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
    :param str: a non-empty string
    :return: a string formed by looping segments of string str
    """
    result = ""
    for i in range(len(str)):
        result += str[:i+1]
    return result