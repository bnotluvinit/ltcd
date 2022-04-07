import unittest


def solution(nums):
    sums = []
    tmp = 0
    for i in nums:
        tmp += i
        sums.append(tmp)

    return sums

class Test(unittest.TestCase):

    def test_1(self):
        nums = [1, 2, 3, 4]
        expected_result = [1, 3, 6, 10]
        actual_result = solution(nums)
        self.assertEqual(expected_result, actual_result)

    def test_2(self):
        nums = [3, 1, 2, 10, 1]
        expected_result = [3, 4, 6, 16, 17]
        actual_result = solution(nums)
        self.assertEqual(expected_result, actual_result)