import unittest


def solution(haystack, needle):
    if haystack is None or needle is None:
        return -1
    if haystack == needle:
        return 0
    needle_length = len(needle)
    for i in range(len(haystack) - needle_length + 1):
        if haystack[i: i + needle_length] == needle:
            return i
    return -1


class Test(unittest.TestCase):

    def test_1(self):
        haystack = "hello"
        needle = "ll"
        actual_result = solution(haystack, needle)
        expected_result = 2
        self.assertEqual(expected_result, actual_result)
