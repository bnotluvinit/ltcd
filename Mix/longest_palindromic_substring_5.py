import unittest


def solution(s):
    longest = ''

    for i in range(len(s)):
        s1 = find_longest(s, i, i)
        if len(s1) > len(longest):
            longest = s1
        s2 = find_longest(s, i, i+1)
        if len(s2) > len(longest):
            longest = s2
    return longest

def find_longest(s, left, right):
    while left > 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1: right]

class Test(unittest.TestCase):

    def test_1(self):
        s = "babad"
        expected_result = "aba"
        actual_result = solution(s)
        self.assertEqual(expected_result, actual_result)


