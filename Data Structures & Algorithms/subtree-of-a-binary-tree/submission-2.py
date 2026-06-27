# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p,q):
            if not p and not q:
                return True
            elif not p or not q or p.val!=q.val:
                return False
            else:
                return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
        
        dq = deque()
        dq.append(root)
        while dq:
            node = dq.popleft()
            if isSameTree(node,subRoot):
                return True
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        return False