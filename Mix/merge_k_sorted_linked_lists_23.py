import unittest
from heapq import heappush, heappop


class ListNode(object):
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.next = nextNode

def solution(lists):
    heap = []
    root = res = ListNode(None)
    for l in lists:
        while l:
            heappush(heap, l.val)
            l = l.next
        while heap:
            res.next = ListNode(heappop(heap))
            res = res.next
        root.next

class Test(unittest.TestCase):

    def test_1(self):
        lists = [[1,4,5],[1,3,4],[2,6]]
        expected_result = [1,1,2,3,4,4,5,6]
        actual_result = solution(lists)
        self.assertEqual(expected_result, actual_result)