# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        

        def traverse(node):
            if node is None:
                return 0, float('-inf'), float('-inf')

            sum_l, local_l, max_node_l = traverse(node.left)
            sum_r, local_r, max_node_r = traverse(node.right)
            
            cur_sum = max(sum_l, sum_r, 0) + node.val

            local = max(
                local_l,
                local_r,
                max(sum_l, 0) + node.val + max(sum_r, 0),
            )

            return cur_sum, local, max(max_node_r, max_node_l, node.val)

        
        return max(traverse(root))