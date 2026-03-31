# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # def size(node):
        #     if not node:
        #         return 0
            
        #     return 1+size(node.left)+size(node.right)
        # s = size(root.left)+1 
        # if k==s:
        #     return root.val
        # elif k>s:
        #     return self.kthSmallest(root.right,k-s)
        # else: return self.kthSmallest(root.left,k)
        def midtriverse(root,val_list):
            if not root:
                return
            midtriverse(root.left,val_list)
            val_list.append(root.val)
            midtriverse(root.right,val_list)
        val_list = []
        midtriverse(root,val_list)
        return val_list[k-1]