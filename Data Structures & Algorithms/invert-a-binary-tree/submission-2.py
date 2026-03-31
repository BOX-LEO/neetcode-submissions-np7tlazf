# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            if root.left and root.right:
                root.left ,root.right = self.invertTree(root.right),self.invertTree(root.left)
            elif root.left:
                root.left,root.right = None,self.invertTree(root.left)
            elif root.right:
                root.left,root.right = self.invertTree(root.right),None
        return root
        