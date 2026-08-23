# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def traverse(preorder: List[int], inorder: List[int]):
            if not preorder and not inorder:
                return None
            val = preorder[0]
            cur = TreeNode(preorder[0])
            mid = inorder.index(preorder[0])
            cur.left = traverse(preorder[1:mid + 1], inorder[:mid])
            cur.right = traverse(preorder[mid + 1:], inorder[mid + 1:])
            return cur
        return traverse(preorder, inorder)
        