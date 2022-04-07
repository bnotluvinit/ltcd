import unittest


def solution(nums):
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return fast

class Test(unittest.TestCase):

    def test_1(self):
        nums = [1,3,4,2,2]
        expected_result = 2
        actual_result = solution(nums)
        self.assertEqual(expected_result, actual_result)

    def test_2(self):
        nums = [3,1,3,4,2]
        expected_result = 3
        actual_result = solution(nums)
        self.assertEqual(expected_result, actual_result)