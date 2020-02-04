def middle_way(a, b):
    """
    Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]
    :param a: an array of 3 ints
    :param b: an array of 3 ints
    :return: an array of 2 ints, the middle elements of a and b
    """
    return [a[1], b[1]]