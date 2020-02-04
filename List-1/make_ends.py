def make_ends(nums):
    """
    Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.

make_ends([1, 2, 3]) → [1, 3]
make_ends([1, 2, 3, 4]) → [1, 4]
make_ends([7, 4, 6, 2]) → [7, 2]
    :param nums: an array of ints, length 1 or more
    :return: an array of 2 ints containing the first and last elements of nums
    """
    return [nums[0], nums[len(nums) - 1]]