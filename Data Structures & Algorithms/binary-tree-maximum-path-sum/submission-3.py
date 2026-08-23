# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def traverse(root):
            nonlocal res
            if root is None:
                return float('-inf')
            
            l_max = traverse(root.left)
            r_max = traverse(root.right)
            res = max(res, l_max, r_max, root.val, root.val + l_max + r_max, root.val + l_max, root.val + r_max)

            return max(root.val, root.val + l_max, root.val + r_max)

        
        res = max(traverse(root), res)
        return res