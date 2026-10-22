# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0 

        def height(node):
            if node is None:
                return - 1
            nonlocal diameter
            left_h = height(node.left)
            right_h = height(node.right)
            diameter = max(diameter , left_h + right_h + 2)

            return 1 + max(left_h , right_h)

        height(root)
        return diameter
        