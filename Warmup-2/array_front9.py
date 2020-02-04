def array_front9(nums):
    """
    Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
    :param nums: an array of ints
    :return: boolean, true if one of the first four elements in the array is a 9
    """
    if len(nums) < 4:
        loop = len(nums)
    else:
        loop = 4
    for i in range(loop):
        if nums[i] == 9:
            return True
    return False