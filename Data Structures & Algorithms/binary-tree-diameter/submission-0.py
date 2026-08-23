# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def get_depth(depth: int, root: Optional[TreeNode]) -> int:
            if root is None:
                return depth - 1
            return max(get_depth(depth + 1, root.right), get_depth(depth + 1, root.left))
        
        if root is None:
            return 0
        l_max = get_depth(1, root.left)
        r_max = get_depth(1, root.right)
        s = l_max + r_max
        return max(s, max(self.diameterOfBinaryTree(root.right), self.diameterOfBinaryTree(root.left)))