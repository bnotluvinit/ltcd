import unittest

class ListNode:
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.next = nextNode


def solution(l1: ListNode, l2: ListNode) -> ListNode:
    # Check if either of the lists is null
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    # Choose head which is smaller of the two lists
    if l1.val < l2.val:
        temp = head = ListNode(l1.val)
        l1 = l1.next
    else:
        temp = head = ListNode(l2.val)
        l2 = l2.next
    # Loop until any of the list becomes null
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            temp.next = ListNode(l1.val)
            l1 = l1.next
        else:
            temp.next = ListNode(l2.val)
            l2 = l2.next
        temp = temp.next
    # Add all the nodes in l1, if remaining
    while l1 is not None:
        temp.next = ListNode(l1.val)
        l1 = l1.next
        temp = temp.next
    # Add all the nodes in l2, if remaining
    while l2 is not None:
        temp.next = ListNode(l2.val)
        l2 = l2.next
        temp = temp.next
    return head

class Test(unittest.TestCase):

    def test_1(self):
        l1 = [1,2,4]
        l2 = [1,3,4]
        expected_result = [1,1,2,3,4,4]
        actual_result = solution(l1, l2)
        self.assertEqual(expected_result, actual_result)