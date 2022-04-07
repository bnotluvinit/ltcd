import unittest


def solution(s):
    openers_to_closers = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    openers = openers_to_closers.keys()
    closers = openers_to_closers.values()

    openers_stack = []

    for char in s:
        if char in openers:
            openers_stack.append(char)
        elif char in closers:
            if not openers_stack:
                return False
            else:
                last_unclosed_opener = openers_stack.pop()

                if not openers_to_closers[last_unclosed_opener] == char:
                    return False

    return openers_stack == []



class Test(unittest.TestCase):

    def test_1(self):
        s = "()[]{}"
        expected_result = True
        actual_result = solution(s)
        self.assertEqual(expected_result, actual_result)
