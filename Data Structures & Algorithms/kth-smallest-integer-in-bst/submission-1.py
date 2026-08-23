# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(root, cnt=0):
            if root is None:
                return (cnt, None)
            if root.left is None and root.right is None:
                return (cnt + 1, root if cnt + 1 == k else None)

            left_cnt, potential_sol_l = helper(root.left, cnt)
            right_cnt, potential_sol_r = helper(root.right, left_cnt + 1)
            potential_sol_center = root if left_cnt + 1 == k else None
            return (right_cnt, potential_sol_l or potential_sol_r or potential_sol_center)

        res = helper(root, 0)
        return res[1].val

