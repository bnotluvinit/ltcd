import unittest

class ListNode:
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.next = nextNode


def solution(l1: ListNode, l2: ListNode) -> ListNode:

    head = ListNode()
    current = head

    while l1 != None and l2 != None:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next

        if l1 != None:
            current.next = l1

        if l2 != None:
            current.next = l2

        return head.next

class Test(unittest.TestCase):

    def test_1(self):
        l1 = [1,2,4]
        l2 = [1,3,4]
        expected_result = [1,1,2,3,4,4]
        actual_result = solution(l1, l2)
        self.assertEqual(expected_result, actual_result)