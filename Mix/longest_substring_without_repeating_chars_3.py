import unittest


def solution(s):
    if s == "":
        return 0
    start = 0
    end = 0
    max_length = 0
    unique_chars = set()
    while end < len(s):
        if s[end] not in unique_chars:
            unique_chars.add(s[end])
            end +=1
            max_length = max(max_length, len(unique_chars))
        else:
            unique_chars.remove(s[start])
            start +=1

    return max_length

class Test(unittest.TestCase):

    def test_1(self):
        s = "abcabcbb"
        expected_result = 3
        actual_result = solution(s)
        self.assertEqual(expected_result, actual_result)

    def test_2(self):
        s = "bbbbb"
        expected_result = 1
        actual_result = solution(s)
        self.assertEqual(expected_result, actual_result)
