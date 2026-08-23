# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = None
        cur = head
        while cur:
            next = cur.next
            cur.next = last
            last = cur
            cur = next
        
        return last