import unittest
from collections import defaultdict


def solution(nums):
    count = 0
    visited = defaultdict(list)

    for i, num in enumerate(nums):
        if num in visited:
            count += len(visited[num])
        visited[num].append(i)
    return count


class Test(unittest.TestCase):

    def test_1(self):
        nums = [1,2,3,1,1,3]
        expected_result = 4
        actual_result = solution(nums)
        self.assertEqual(expected_result, actual_result)