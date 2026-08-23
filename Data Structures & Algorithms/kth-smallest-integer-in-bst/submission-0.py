# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = []
        def traverse(root):
            if len(l) >= k:
                return
            if root is None:
                return
            traverse(root.left)
            l.append(root.val)
            traverse(root.right)
        traverse(root)
        return l[k - 1]