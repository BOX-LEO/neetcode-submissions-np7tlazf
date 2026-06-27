# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.seen = []
        def mid_traversal(node):
            if node:
                mid_traversal(node.left)
                self.seen.append(node.val)
                mid_traversal(node.right)
        mid_traversal(root)
        return self.seen[k-1]
