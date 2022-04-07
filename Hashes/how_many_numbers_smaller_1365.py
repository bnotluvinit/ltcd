import unittest


def solution(nums):
    length = len(nums)
    ans = []
    count = 0
    for i in nums:
        for j in range(length):
            if (nums[j] - i) < 0:
                count += 1
        ans.append(count)
        count = 0
    return ans



class Test(unittest.TestCase):

    def test_1(self):
        nums = [8,1,2,2,3]
        expected_result = [4,0,1,1,3]
        actual_result = solution(nums)
        self.assertEqual(expected_result, actual_result)

    def test_2(self):
        nums = [6, 5, 4, 8]
        expected_result = [2,1,0,3]
        actual_result = solution(nums)
        self.assertEqual(expected_result, actual_result)