# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def depth(root):
            if not root:
                return 0
            return 1+ max(depth(root.left),depth(root.right))
        d = depth(root)

        if d == 0:
            return []
        else: 
            result = []
            cur_level = [root]
            for _ in range(d):
                result.append([i.val for i in cur_level])
                next_level = []
                for i in cur_level:
                    if i.left:
                        next_level.append(i.left)
                    if i.right:
                        next_level.append(i.right)
                cur_level = next_level
        
        return result
                