import unittest


def solution(nums):
    return [nums[nums[i]] for i in range(len(nums))]


class Test(unittest.TestCase):

    def test_1(self):
        nums = [0, 2, 1, 5, 3, 4]
        expected_result = [0, 1, 2, 4, 5, 3]
        actual_result = solution(nums)
        self.assertEqual(actual_result, expected_result)