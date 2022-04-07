import unittest


def solution(nums, target):
    values = {}
    for inx, value in enumerate(nums):
        if target - value in values:
            return [values[target - value], inx]
        else:
            values[value] = inx


class Test(unittest.TestCase):

    def test_1(self):
        nums = [2,7,11,15]
        target = 9
        expected_result = [0,1]
        actual_result = solution(nums, target)
        self.assertEqual(expected_result, actual_result)

    def test_2(self):
        nums = [3,2,4]
        target = 6
        expected_result = [1,2]
        actual_result = solution(nums, target)
        self.assertEqual(expected_result, actual_result)