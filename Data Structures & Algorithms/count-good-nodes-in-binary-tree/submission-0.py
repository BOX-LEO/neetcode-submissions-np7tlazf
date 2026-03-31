# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.result = 0
        mx = root.val
        def dfs(root,mx):
            if not root:
                return
            if root.val>=mx:
                self.result+=1
                mx = root.val
            dfs(root.left,mx)
            dfs(root.right,mx)
        dfs(root,mx)
        return self.result
            

        