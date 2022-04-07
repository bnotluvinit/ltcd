import unittest


def solution(cost):
    cost.sort()
    cost.reverse()

    total = 0
    N = len(cost)
    for i in range(N):
        if i % 3 != 2:
            total += cost[i]
    return total

class Test(unittest.TestCase):

    def test_1(self):
        cost = [6,5,7,9,2,2]
        expected_result = 23
        actual_result = solution(cost)
        self.assertEqual(expected_result, actual_result)

    def test_2(self):
        cost = [1,2,3]
        expected_result = 5
        actual_result = solution(cost)
        self.assertEqual(expected_result, actual_result)