import unittest


def find_first_occurance(nums, target):
    first_occurance = -1
    left, right = 0, len(nums) - 1

    while left <= right:
        middle = left + (right - left) // 2

        if nums[middle] == target:
            first_occurance = middle
            right = middle - 1
        elif target < nums[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return first_occurance

def find_last_occurance(nums, target):
    last_occurance = -1
    left, right = 0, len(nums) - 1

    while left <= right:
        middle = left + (right - left) // 2
        if nums[middle] == target:
            last_occurance = middle
            left = middle + 1

        if target < nums[middle]:
            right = right - 1

        else:
            left = middle + 1
    return last_occurance


def solution(nums, target):
    return [find_first_occurance(nums, target), find_last_occurance(nums, target)]




class Test(unittest.TestCase):

    def test_1(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        expected_result = [3,4]
        actual_result = solution(nums, target)
        self.assertEqual(expected_result, actual_result)

    def test_2(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 6
        expected_result = [-1, -1]
        actual_result = solution(nums, target)
        self.assertEqual(expected_result, actual_result)