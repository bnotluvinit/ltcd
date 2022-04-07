import unittest
from collections import Counter


def solution(nums1, nums2, nums3):
    count = Counter()
    for nums in nums1, nums2, nums3:
        count.update(set(nums))
    return [i for i, c in count.items() if c >=2]

class Test(unittest.TestCase):

    def test_1(self):
        nums1 = [1,1,3,2]
        nums2 = [2,3]
        nums3 = [3]
        expected_result = [3,2]
        actual_result = solution(nums1, nums2, nums3)
        self.assertEqual(expected_result, actual_result)