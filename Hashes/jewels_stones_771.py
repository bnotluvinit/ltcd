import unittest


def solution(jewels, stones):
    jewel_counter = 0
    jewel_table = set()

    for jewel in jewels:
        jewel_table.add(jewel)

    for stone in stones:
        if stone in jewel_table:
            jewel_counter += 1
    return jewel_counter


class Test(unittest.TestCase):

    def test_1(self):
        jewels = "aA"
        stones = "aAAbbbb"
        expected_result = 3
        actual_result = solution(jewels, stones)
        self.assertEqual(expected_result, actual_result)

    def test_2(self):
        jewels = "z"
        stones = "ZZ"
        expected_result = 3
        actual_result = solution(jewels, stones)
        self.assertEqual(expected_result, actual_result)