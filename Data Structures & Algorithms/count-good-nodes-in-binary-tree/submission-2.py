# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def find_gn(node,local_max):
            if not node:
                return
            if node.val>=local_max:
                self.ans+=1
                local_max = node.val
            find_gn(node.left,local_max)
            find_gn(node.right,local_max)
        find_gn(root,root.val)
        return self.ans

