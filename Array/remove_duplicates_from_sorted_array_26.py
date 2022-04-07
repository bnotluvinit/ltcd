import unittest


def solution(nums):
    count = 0
    for i in range(len(nums)):
        # If the current element is equal to the next element we skip
        if i < len(nums) - 2 and nums[i] == nums[i+1]:
            continue
        nums[count] = nums[i]
        count += 1
    return count


class Test(unittest.TestCase):

    def test_1(self):
        nums = [1, 1, 2]
        expected_result = 2
        actual_result = solution(nums)
        self.assertEqual(expected_result, actual_result)

    def test_2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected_resul = 5
        actual_result = solution(nums)
        self.assertEqual(expected_resul, actual_result)