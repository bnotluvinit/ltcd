import unittest


def solution(digits):
    phone_dict = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"}

    # Implement DFS
    def dfs(index, path):
        if len(path) == len(digits):
            result.append(path)
            return
        for i in range(index, len(digits)):
            for j in phone_dict[digits[i]]:
                dfs(i + 1, path + j)

    # Exception handling
    if not digits:
        return []
    # Run dfs
    result = []
    dfs(0, "")
    return result

class Test(unittest.TestCase):

    def test_1(self):
        digits = "23"
        expected_result = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        actual_result = solution(digits)
        self.assertEqual(expected_result, actual_result)

    def test_2(self):
        digits = "2"
        expected_result = ["a", "b", "c"]
        actual_result = solution(digits)
        self.assertEqual(expected_result, actual_result)
