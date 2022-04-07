import unittest


def solution(strs):
    if len(strs) == 0:
        return " "
    elif len(strs) == 1:
        return strs[0]

    m = len(min(strs, key=len))
    i = 0
    reference = strs[0]

    while i < m:
        for str in strs:
            if str[i] != reference[i]:
                return reference[:i]
        i +=1

    return reference[:m]

class Test(unittest.TestCase):

    def test_1(self):
        strs = ["flower", "flow", "flight"]
        expected_result = "fl"
        actual_result = solution(strs)
        self.assertEqual(expected_result, actual_result)
