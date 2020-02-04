def has23(nums):
    """
    Given an int array length 2, return True if it contains a 2 or a 3.

has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False
    :param nums: an array of 2 ints
    :return: boolean, True if nums contains a 2 or a 3
    """
    return nums.count(2) + nums.count(3) > 0