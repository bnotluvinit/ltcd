import unittest


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solution(l1, l2):
    head = l3 = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        l3.val = carry % 10
        carry = carry // 10
        if l1 or l2 or carry:
            l3.next = ListNode(0)
            l3 = l3.next
    return head


class Test(unittest.TestCase):

    def test_1(self):
        l1 = [2,4,3]
        l2 = [5,6,4]
        expected_result = [7,0, 8]
        actual_result = solution(l1, l2)
        self.assertEqual(expected_result, actual_result)

    def test_2(self):
        nums = [3,1,3,4,2]
        expected_result = 3
        actual_result = solution(nums)
        self.assertEqual(expected_result, actual_result)