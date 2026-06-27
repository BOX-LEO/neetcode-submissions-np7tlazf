# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def find_lca(node,p,q):
            if not node:
                return False
            l,r = find_lca(node.left,p,q),find_lca(node.right,p,q)
            if l and r:
                self.ans = node
                return True
            if node.val ==p.val or node.val ==q.val:
                if l or r:
                    self.ans = node
                return True
            return l or r
        find_lca(root,p,q)

        return self.ans