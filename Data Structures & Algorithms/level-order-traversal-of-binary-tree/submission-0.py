# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = deque()
        res = []
        q.append((root, 0))

        while len(q) > 0:
            top, l = q.pop()
            if top is None:
                continue
            if l >= len(res):
                res.append([])
            res[l].append(top.val)
            q.append((top.right, l + 1))
            q.append((top.left, l + 1))
        
        return res

