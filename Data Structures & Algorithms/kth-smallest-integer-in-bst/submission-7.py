# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        res = None

        def helper(root):
            nonlocal cnt, res

            if root is None or res is not None:
                return

            helper(root.left)
            if res is not None:
                return

            cnt += 1
            if cnt == k:
                res = root.val
                return

            helper(root.right)
        
        helper(root)
        return res

