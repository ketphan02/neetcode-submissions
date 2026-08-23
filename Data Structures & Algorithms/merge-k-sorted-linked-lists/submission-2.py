# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __lt__(self, other: 'ListNode'):
        return self.val < other.val

from heapq import heappush, heappop, heapify

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = [l for l in lists if l is not None]
        heapify(h)
        dummy = ListNode()
        cur = dummy
        while h:
            top = heappop(h)
            cur.next = top
            cur = cur.next
            top = top.next
            if top is not None:
                heappush(h, top)
        
        return dummy.next