# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balance = True
        def height(node):
            if not node:
                return 0
            left_h = height(node.left)
            right_h = height(node.right)
            if abs(left_h-right_h)>1:
                self.balance = False
            return 1+max(left_h,right_h)
        height(root)
        return self.balance
        

        
        