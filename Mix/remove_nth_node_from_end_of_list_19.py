import unittest

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solution(head, n):
    size = 0
    new_head, dummy_head = head
    while head:
        size +=1
        head = head.next
    stop = size - n
    if stop == 0:
        return new_head.next
    counter = 1
    while dummy_head:
        if counter == stop:
            dummy_head.next = dummy_head.next.next
            return new_head
        counter += 1
        dummy_head = dummy_head.next


class Test(unittest.TestCase):

    def test_1(self):
        head = [1,2,3,4,5]
        n = 2
        expected_result = [1,2,3,5]
        actual_result = solution(head, n)

        self.assertEqual(expected_result, actual_result)