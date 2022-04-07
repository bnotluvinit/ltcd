import unittest


def solution(num):
    n = len(num) - 1
    while (n > 0):
        if (int(num[n]) % 2 != 0):
            return num[0:n + 1]
        else:
            n -= 1
    if (n == 0):
        if (int(num[n]) % 2 != 0):
            return num[0];
        else:
            return ""


class Test(unittest.TestCase):

    def test_1(self):
        nums = "52"
        expected_result = "5"
        actual_result = solution(nums)
        self.assertEqual(expected_result, actual_result)

    def test_2(self):
        nums = "4206"
        expected_result = ""
        actual_result = solution(nums)
        self.assertEqual(expected_result, actual_result)
