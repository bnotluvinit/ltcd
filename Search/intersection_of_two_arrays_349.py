import unittest


def solution(nums1, nums2):
    return list(set(nums1) & set(nums2))


class Test(unittest.TestCase):

    def test_1(self):
        nums1 = [1,2,2,1]
        nums2 = [2,2]
        expected_result = [2]
        actual_result = solution(nums1, nums2)
        self.assertEqual(expected_result, actual_result)

    def test_2(self):
        nums1 = [4,9,5]
        nums2 = [9,4,9,8,4]
        expected_result = [9,4]
        actual_result = solution(nums1, nums2)
        self.assertEqual(expected_result, actual_result)