# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse linked list
        cur = slow.next
        prev = slow.next = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        # merge
        a, b = head, prev
        while a and b:
            tmp_a_next, tmp_b_next = a.next, b.next
            a.next, b.next = b, tmp_a_next
            a, b = tmp_a_next, tmp_b_next
        
            
