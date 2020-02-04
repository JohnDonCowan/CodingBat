def hello_name(name):
    """
    Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".


hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'
    :param name: a string
    :return: a string, a greeting in the form of "Hello <name>!"
    """
    return "Hello " + name + "!"