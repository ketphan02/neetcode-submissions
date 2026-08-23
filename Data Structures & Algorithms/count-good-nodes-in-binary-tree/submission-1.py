# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root: Optional[TreeNode], num: int) -> int:
            if root is None:
                return 0
            res = 0
            if root.val >= num:
                num = root.val
                res = 1
            return res + helper(root.left, num) + helper(root.right, num)
        
        return helper(root, float("-inf"))