import unittest


def solution(s):
    result = []
    p,q = 0,0
    quote_started = False

    while q < len(s):
        if q == len(s) - 1:
            if s[p] != " ":
                result.append(s[p:q + 1]) # last one
        else:
            if s[q] == " " and not quote_started:
                if s[p] != " ":
                    result.append(s[p:q])
                p = q + 1
            elif s[q] == "\"":  # check all types of edge cases
                quote_started = not quote_started
        q += 1

    if quote_started:
        raise ValueError('Input has incorrect quotes')


    return result


class Test(unittest.TestCase):

    def test_1(self):
        string = 'foo hello "hello world" blah'
        expected_result = ["foo", "hello", "hello world", "blah"]
        actual_result = solution(string)
        self.assertEqual(expected_result, actual_result)
