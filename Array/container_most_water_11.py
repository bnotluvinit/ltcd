import unittest


def solution(height):
    left = 0
    right = len(height) - 1
    result = 0

    while left < right:
        water = (right - left) * min(height[left], height[right])
        if water > result:
            result = water
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return result


class Test(unittest.TestCase):

    def test_1(self):
        height = [1,8,6,2,5,4,8,3,7]
        expected_result = 49
        actual_result = solution(height)
        self.assertEqual(expected_result, actual_result)