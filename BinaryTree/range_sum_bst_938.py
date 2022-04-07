import unittest

from BinaryTree.binary_tree import TreeNode


def solution(root, low, high):
    ans = 0
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            if low <= node.value <= high:
                ans += node.value
            if low < node.value:
                stack.append(node.left)
            if node.value < high:
                stack.append(node.right)


class Test(unittest.TestCase):

    def test_1(self):
        root = TreeNode(10)
        root.insert(5)
        root.insert(15)
        root.insert(3)
        root.insert(7)
        root.insert(18)
        root.PrintTree()
        low = 7
        high = 15
        expected_result = 32
        actual_result = solution(root, low, high)
        self.assertEqual(expected_result, actual_result)