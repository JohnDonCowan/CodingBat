def max_end3(nums):
    """
Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.

max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
    :param nums: an array of 3 ints
    :return: an array of 3 of the largest value of the first or last element of nums
    """
    large = max(nums[0], nums[2])
    return [large, large, large]