# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import functools

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        @functools.cache
        def get_depth(d, root) -> int:
            if root is None:
                return d - 1
            return max(get_depth(d + 1, root.right), get_depth(d + 1, root.left))
        
        if root is None:
            return True
        
        l = get_depth(1, root.left)
        r = get_depth(1, root.right)
        if abs(l - r) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)