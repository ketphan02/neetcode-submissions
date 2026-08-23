# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        if self.val == other.val:
            return 0
        return self.val < other.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        for l in lists:
            if l:
                heapq.heappush(h, (l.val, l))

        head = ListNode()
        cur = head
        while h:
            _, top = heapq.heappop(h)
            cur.next = top
            top = top.next
            if top:
                heapq.heappush(h, (top.val, top))
            cur = cur.next
        return head.next
