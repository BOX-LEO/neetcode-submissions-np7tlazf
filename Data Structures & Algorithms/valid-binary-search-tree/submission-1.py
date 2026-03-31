# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root,mi,mx):
            if not root:
                return True
            if not (mi<root.val<mx):
                return False
            else: return valid(root.left,mi,root.val) and valid(root.right,root.val,mx)
        return valid(root,-1001,1001)
                    
            