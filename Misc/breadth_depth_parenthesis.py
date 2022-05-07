import unittest


def has_valid_parenthesis(input):
    parens = []
    for position in range(len(input)):
        if input[position] == '(':
            parens.append('(')
        elif input[position] == ')':
            last_parens = parens.pop()
            if last_parens is None:
                return False

    return len(parens) == 0

def max_depth(input):
    parens = []
    max_depth = 0

    for position in range(len(input)):
        if input[position] == '(':
            parens.append('(')
        elif input[position] == ')':
            if len(parens) > max_depth:
                max_depth = len(parens)
            parens.pop()
    return max_depth


def max_breadth(input):
    parens = []
    max_breadth = 0

    for position in range(len(input)):
        if input[position] == '(':
            parens.append('(')
        elif input[position] == ')':
            parens.pop()

        if len(parens) == 0:
            max_breadth += 1

    return max_breadth


class Solution:
    def maxDepth(self, s):
        ans=0
        tmp=0
        for i in s:
            if (i=='('):
                tmp+=1
                ans=max(ans,tmp)
            elif(i==')'):
                tmp-=1
                ans=max(ans,tmp)
        return ans


# Function to find the length of the longest balanced parenthesis in a string
def findMaxLen(s):
    # base case
    if not s:
        return 0

    # create a stack of integers for storing an index of parenthesis in the string
    stack = deque()

    # initialize the stack by -1
    stack.append(-1)

    # stores the length of the longest balanced parenthesis
    length = 0

    # iterate over the characters of the string
    for i, e in enumerate(s):

        # if the current character is an opening parenthesis,
        # push its index in the stack
        if e == '(':
            stack.append(i)

        # if the current character is a closing parenthesis
        else:
            # pop the top index from the stack
            stack.pop()

            # if the stack becomes empty, push the current index into the stack
            if not stack:
                stack.append(i)
                continue

            # get the length of the longest balanced parenthesis ending at the
            # current character
            curr_len = i - stack[-1]

            # update the length of the longest balanced parenthesis
            if length < curr_len:
                length = curr_len

    return length

def max_square(matrix):
    if not matrix:
        return 0
    R = len(matrix)
    C = len(matrix[0])
    dp = [[0]*C for _ in range(R)]
    mx_count = 0
    for i in range(R):
        for j in range(C):
            dp[i][j] = int(matrix[i][j])
            if dp[i][j]:
                mx_count = 1
    for i in range(1,R):
        for j in range(1,C):
            if dp[i][j] and dp[i-1][j] and dp[i][j-1] and dp[i-1][j-1]:
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                mx_count = dp[i][j] if dp[i][j]>mx_count else mx_count
    return mx_count**2
class Test(unittest.TestCase):

    def test_1(self):
        s = "()"
        actual_result = has_valid_parenthesis(s)
        self.assertTrue(actual_result)

    def test_2(self):
        s = "((("
        actual_result = has_valid_parenthesis(s)
        self.assertFalse(actual_result)

    def test_3(self):
        s = "(())"
        actual_result = max_depth(s)
        expected_result = 1
        self.assertEqual(actual_result, expected_result)

    def test_4(self):
        s = "((), ())"
        actual_result = max_breadth(s)
        expected_result = 2
        self.assertEqual(actual_result, expected_result)