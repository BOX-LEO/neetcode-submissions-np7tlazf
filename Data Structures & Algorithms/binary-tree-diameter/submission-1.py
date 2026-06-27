# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def depth(node):
            nonlocal ans
            if not node:
                return -1
            else:
                l = depth(node.left)+1
                r = depth(node.right)+1
                if ans<l+r:
                    ans = l+r
                return max(l,r)
        depth(root)
        return ans
