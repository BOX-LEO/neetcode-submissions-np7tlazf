# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        root = TreeNode(val = preorder[0])
        left = inorder.index(preorder[0])
        left_pre = preorder[1:1+left]
        left_in = inorder[:left]
        right_pre = preorder[1+left:]
        right_in = inorder[1+left:]
        root.left = self.buildTree(left_pre,left_in)
        root.right = self.buildTree(right_pre,right_in)
        return root