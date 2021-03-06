def array_count9(nums):
    """
Given an array of ints, return the number of 9's in the array.

array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
    :param nums: an array of ints
    :return: an int of the number of 9s in the nums array
    """
    count = 0
    for i in range(len(nums)):
      if nums[i] == 9:
        count += 1
    return count