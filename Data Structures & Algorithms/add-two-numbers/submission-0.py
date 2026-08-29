# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        remainder = 0
        while l1 or l2:
            num = remainder
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            remainder = num // 10
            cur.next = ListNode(num % 10)
            cur = cur.next

        if remainder:
            cur.next = ListNode(remainder)

        return dummy.next