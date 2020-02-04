def make_out_word(out, word):
    """
    Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".

make_out_word('<<>>', 'Yay') → '<<Yay>>'
make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
make_out_word('[[]]', 'word') → '[[word]]'
    :param out: a string of 4 characters
    :param word: a string
    :return: a string with word in the middle of out
    """
    return out[:2] + word + out[2:]