def big_diff(nums):
    """
    Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.

big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8
    :param nums: an array of 1 or more ints
    :return: int, difference between the largest and smallest values in the array
    """
    small = nums[0]
    large = nums[0]
    for num in nums:
        small = min(small, num)
        large = max(large, num)
    return large - small