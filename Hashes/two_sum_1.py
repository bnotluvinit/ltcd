import unittest


def solution(nums, target):
    values = {}
    for idx, value in enumerate(nums):
        if target - value in values:
            return [values[target - value], idx]
        else:
            values[value] = idx


class Test(unittest.TestCase):

    def test_1(self):
        nums = [2,7,11,15]
        target = 9
        expected_result = [0, 1]
        actual_result = solution(nums, target)
        self.assertEqual(expected_result, actual_result)