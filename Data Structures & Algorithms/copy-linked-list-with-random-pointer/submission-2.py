"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        h = {}

        def copy(node):
            if not node:
                return None
            if node in h:
                return h[node]

            h[node] = Node(node.val)
            h[node].next = copy(node.next)
            h[node].random = copy(node.random)
        
            return h[node]

        return copy(head)