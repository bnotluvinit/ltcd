import unittest

def solution(nums):
    return nums * 2

class Test(unittest.TestCase):

    def test_1(self):
        nums = [1, 2, 1]
        expected_result = [1, 2, 1, 1, 2, 1]
        actual_result = solution(nums)
        self.assertEqual(expected_result, actual_result)
