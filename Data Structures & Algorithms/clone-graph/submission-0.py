"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = {}
        
        def deepcopy(node: Optional['Node']):
            nonlocal cloned

            if not node:
                return None
            cur = Node(node.val, [])
            cloned[cur.val] = cur

            for nei in node.neighbors:
                if nei.val in cloned:
                    cur.neighbors.append(cloned[nei.val])
                else:
                    cur.neighbors.append(deepcopy(nei))
            return cur
        
        return deepcopy(node)