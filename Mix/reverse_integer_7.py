import unittest


def solution(x):
    isNegative = False
    if x < 0:
        isNegative = True
        x = -x
    reversedNumber = 0
    while x:
        reversedNumber = reversedNumber * 10 + x % 10
        x //= 10
    if reversedNumber >= 2 ** 31 - 1 or reversedNumber <= -2 ** 31:
        return 0
    return -reversedNumber if isNegative else reversedNumber


class Test(unittest.TestCase):

    def test_1(self):
        x = 123
        expected_result = 321
        actual_result = solution(x)
        self.assertEqual(expected_result, actual_result)
