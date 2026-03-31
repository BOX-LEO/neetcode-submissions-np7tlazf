# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def iot(node):
            if not node.left and not node.right:
                res.append(node.val)
                return
            if node.left:
                iot(node.left)
            res.append(node.val)
            if node.right:
                iot(node.right)
        iot(root)
        return res[k-1]
