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
        hsh = {}
        
        cur = head

        def deepcopy(node):
            nonlocal hsh
            if node is None:
                return None
            
            next = node.next
            rand = node.random

            key = (node.val, next.val if next else None, rand.val if rand else None)
            if key in hsh:
                return hsh[key]

            new_node = Node(node.val)
            hsh[key] = new_node
            hsh[key].next = deepcopy(next)
            hsh[key].random = deepcopy(rand)
            
            return hsh[key]
        
        return deepcopy(head)





