# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checker(start, end, root):
            if root is None:
                return True
            if root.val <= start or root.val >= end:
                return False
            
            return checker(start, root.val, root.left) and checker(root.val, end, root.right)

        
        return checker(float('-inf'), float('inf'), root)
            