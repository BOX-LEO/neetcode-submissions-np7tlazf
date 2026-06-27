# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balance = True
        def balanced_depth(node):
            if not node:
                return 0
            else:
                l = balanced_depth(node.left)
                r = balanced_depth(node.right)
                if abs(l-r)>1:
                    self.balance = False
                return max(l,r)+1

        balanced_depth(root)
        return self.balance