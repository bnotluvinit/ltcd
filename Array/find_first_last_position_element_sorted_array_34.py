import unittest

def find_first_occurance(nums, target):
    # Left snd right pointers
    left, right = 0, len(nums) - 1
    # Index of first occurrence
    first_occurrence = -1
    # Loop until the two pointers meet
    while left <= right:
        # Middle index
        middle = left + (right - left) // 2
        # Check if we have found the value
        if target == nums[middle]:
            first_occurrence = middle
            right = middle - 1
        # If the target is less than the element
        # at the middle index
        elif target < nums[middle]:
            right = middle - 1
        # If the target is greater than the element
        # at the middle index
        else:
            left = middle + 1
    return first_occurrence


def find_last_occurance(nums, target):
    # Left snd right pointers
    left, right = 0, len(nums) - 1
    # Index of first occurrence
    last_occurrence = -1
    # Loop until the two pointers meet
    while left <= right:
        # Middle index
        middle = left + (right - left) // 2
        # Check if we have found the value
        if target == nums[middle]:
            last_occurrence = middle
            left = middle + 1
        # If the target is less than the element
        # at the middle index
        elif target < nums[middle]:
            right = middle - 1
        # If the target is greater than the element
        # at the middle index
        else:
            left = middle + 1
    return last_occurrence


def solution(nums, target):
    return [find_first_occurance(nums, target), find_last_occurance(nums, target)]

class Test(unittest.TestCase):

    def test_1(self):
        nums = [5,7,7,8,8,10]
        target = 8
        expected_result = [3, 4]
        actual_result = solution(nums, target)
        self.assertEqual(expected_result, actual_result)