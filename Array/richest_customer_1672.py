import unittest

def solution(accounts):
    ans, curr = 0, 0
    for i in accounts:
        for j in i:
            curr += j
        ans = max(ans, curr)
        curr = 0
    return ans

class Test(unittest.TestCase):

    def test_1(self):
        accounts = [[1,2,3],[3,2,1]]
        expected_result = 6
        actual_result = solution(accounts)
        self.assertEqual(expected_result, actual_result)

    def test_2(self):
        accounts = [[2, 8,7], [7,1,3], [1,9,5]]
        expected_result = 17
        actual_result = solution(accounts)
        self.assertEqual(expected_result, actual_result)