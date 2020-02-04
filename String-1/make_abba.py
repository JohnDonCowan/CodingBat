def make_abba(a, b):
    """
    Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

make_abba('Hi', 'Bye') → 'HiByeByeHi'
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
make_abba('What', 'Up') → 'WhatUpUpWhat'
    :param a: a string
    :param b: a string
    :return: a string formed from combining a and b in the form "abba"
    """
    return a+b+b+a