# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = dummy
        for _ in range(n):
            cur = cur.next
        to_rm = dummy
        while cur.next:
            cur = cur.next
            to_rm = to_rm.next
        print(to_rm.val)
        to_rm.next = to_rm.next.next

        return dummy.next
