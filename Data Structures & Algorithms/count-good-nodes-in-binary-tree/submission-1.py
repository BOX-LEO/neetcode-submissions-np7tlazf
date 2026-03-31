# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def isgood(node,max_value):
            nonlocal res
            if node.val>=max_value:
                res+=1
                max_value = node.val
            if node.left:
                isgood(node.left,max_value)
            if node.right:
                isgood(node.right,max_value)
        isgood(root,root.val)
        return res