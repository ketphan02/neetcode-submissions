# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        def helper(root):
            nonlocal stack

            if root is None:
                return None

            helper(root.left)
            if len(stack) >= k:
                return stack[k - 1]

            stack.append(root.val)
            if len(stack) >= k:
                return stack[k - 1]

            helper(root.right)
            if len(stack) >= k:
                return stack[k - 1]
        
        return helper(root)

