# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)
        def _traverse(root, l):
            if root is None:
                return
            levels[l].append(root.val)
            _traverse(root.left, l + 1)
            _traverse(root.right, l + 1)
        
        _traverse(root, 0)

        return list(levels.values())