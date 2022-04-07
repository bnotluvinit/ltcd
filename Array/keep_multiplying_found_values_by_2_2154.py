import unittest


def solution(nums, original):

    while original in nums:
        original *= 2
    return original



class Test(unittest.TestCase):

    def test_1(self):
        nums = [5, 3, 6, 1, 12]
        original = 3
        expected_result = 24
        actual_result = solution(nums, original)
        self.assertEqual(expected_result, actual_result)