import unittest
from collections import Counter


def solution(nums):
    count = Counter(nums)
    ans = 0
    for i in count:
        if count[i] == len(nums) / 2:
            ans = i
        return ans

class Test(unittest.TestCase):

    def test_1(self):
        nums = [1, 2, 3, 3]
        expected_result = 3
        actual_result = solution(nums)
        self.assertEqual(expected_result, actual_result)

    def test_2(self):
        nums = [2, 1, 2, 5, 3, 2]
        expected_result = 2
        actual_result = solution(nums)
        self.assertEqual(expected_result, actual_result)