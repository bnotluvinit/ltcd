import unittest


def solution(s):
    dict = {'L': 0, 'R': 0}
    count = 0
    for word in s:
        dict[word] += 1
        if dict['R'] == dict['L']:
            count += 1
            dict['R'] = 0
            dict['L'] = 0
    return count



class Test(unittest.TestCase):

    def test_1(self):
        s = "RLRRLLRLRL"
        expected_result = 4
        actual_result = solution(s)
        self.assertEqual(expected_result, actual_result)