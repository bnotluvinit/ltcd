import unittest


def solution(allowed, words):

    not_match = 0
    for word in words:
        for w in word:
           if w not in allowed:
                not_match +=1
                break
    ans = len(words) - not_match
    return ans

class Test(unittest.TestCase):

    def test_1(self):
        allowed = "ab"
        words = ["ad","bd","aaab","baa","badab"]
        expected_result = 2
        actual_result = solution(allowed, words)
        self.assertEqual(expected_result, actual_result)

    def test_2(self):
        allowed = "abc"
        words = ["a","b","c","ab","ac","bc","abc"]
        expected_result = 7
        actual_result = solution(allowed, words)
        self.assertEqual(expected_result, actual_result)
