"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        h = {}

        def cloner(node):
            if not node:
                return

            if node in h:
                return h[node.val]

            h[node.val] = Node(node.val)
            for nei in node.neighbors:
                h[node.val].neighbors.append(cloner(nei) if nei.val not in h else h[nei.val])

            return h[node.val]
        
        return cloner(node)