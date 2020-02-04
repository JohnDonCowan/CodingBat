def rotate_left3(nums):
    """
    Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]
    :param nums: an array of 3 ints
    :return: an array of nums elements "rotated left"
    """
    save = nums[0]
    nums.pop(0)
    nums.append(save)
    return nums