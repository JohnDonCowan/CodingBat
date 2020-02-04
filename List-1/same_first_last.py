def same_first_last(nums):
    """
    Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True
    :param nums: array of ints
    :return: boolean, True if the array is at least length 1 and the first and last element are equal
    """
    return (len(nums) > 0 and nums[0] == nums[len(nums) - 1])