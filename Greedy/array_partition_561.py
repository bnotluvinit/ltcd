import unittest


def solution(nums):
    nums.sort()
    res = 0
    while nums:
        res += min(nums.pop(), nums.pop())
    return res


class Test(unittest.TestCase):

    def test_1(self):
        nums = [6,2,6,5,1,2]
        expected_result = 9
        actual_result = solution(nums)
        self.assertEqual(expected_result, actual_result)
