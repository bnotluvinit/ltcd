import unittest


def solution(num):
    return int(str(num).replace('6', '9', 1))


class Test(unittest.TestCase):

    def test_1(self):
        num = 9669
        expected_result = 9969
        actual_result = solution(num)
        self.assertEqual(expected_result, actual_result)

    def test_2(self):
        num = 9996
        expected_result = 9999
        actual_result = solution(num)
        self.assertEqual(expected_result, actual_result)