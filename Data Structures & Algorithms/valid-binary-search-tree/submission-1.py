# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(l, r, root) -> bool:
            if root is None:
                return True
            if l >= root.val or root.val >= r:
                return False
            return helper(l, root.val, root.left) and helper(root.val, r, root.right)
        
        return helper(float('-inf'), float('inf'), root)