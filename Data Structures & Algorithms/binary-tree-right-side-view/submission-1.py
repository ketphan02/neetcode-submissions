# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def inOrderTraversal(root) -> List[List[int]]:
            res = []
            if root is None:
                return res
            q = deque()
            q.append((root, 0))
            while len(q) > 0:
                top, level = q.pop()
                if top is None:
                    continue
                if level >= len(res):
                    res.append([])
                res[level].append(top.val)
                q.append((top.right, level + 1))
                q.append((top.left, level + 1))
            
            return res

        return [l[-1] for l in inOrderTraversal(root)]