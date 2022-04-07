import unittest


def solution(rings):
    rods = [set() for _ in range(10)]
    ans = 0
    for i in range(0, len(rings), 2):
        rods[int(rings[i + 1])].add(rings[i])
    for j in rods:
        if len(j) >= 3:
            ans += 1
    return ans


class Test(unittest.TestCase):

    def test_1(self):
        rings = "B0R0G0R9R0B0G0"
        expected_result = 1
        actual_result = solution(rings)
        self.assertEqual(expected_result, actual_result)

    def test_2(self):
        rings = "G4"
        expected_result = 0
        actual_result = solution(rings)
        self.assertEqual(expected_result, actual_result)