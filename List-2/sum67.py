def sum67(nums):
    """
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
    :param nums: an array of ints; contains a 7 if it contains a 6
    :return: an int, the sum of numbers in nums, except for sections of numbers between a 6 and 7
    """
    toggle = True
    count = 0
    for num in nums:
        if toggle and num != 6:
            count += num
        elif num == 6:
            toggle = False
        elif num == 7:
            toggle = True
    return count