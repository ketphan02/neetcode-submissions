# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2

        if not cur1 and not cur2:
            return None
        elif not cur1:
            return cur2
        elif not cur2:
            return cur1

        head = None
        cur = None
        while cur1 or cur2:
            if head is None:
                if cur1 is None or cur1.val > cur2.val:
                    head = cur2
                    cur = cur2
                    cur2 = cur2.next
                else:
                    head = cur1
                    cur = cur1
                    cur1 = cur1.next
            else:
                if not cur1 and cur2:
                    cur.next = cur2
                    return head
                if not cur2 and cur1:
                    cur.next = cur1
                    return head

                if cur1.val > cur2.val:
                    cur.next = cur2
                    cur = cur.next
                    cur2 = cur2.next
                else:
                    cur.next = cur1
                    cur = cur.next
                    cur1 = cur1.next
        return head
                    