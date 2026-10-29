# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):

            if node is None:
                return True, -1 
            left_b , left = check(node.left)
            right_b, right = check(node.right)
            balanced = (left_b and right_b 
            and abs(left - right) <= 1)
            height = 1 + max( left, right)

            return balanced, height
        return check(root)[0]

        


            
        