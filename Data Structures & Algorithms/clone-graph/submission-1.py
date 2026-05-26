"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        hash = {}
        hash[node] = Node(node.val)
        dq = deque([node])
        while dq:
            n = dq.popleft()
            for neighbor in n.neighbors:
                if neighbor not in hash:
                    dq.append(neighbor)
                    hash[neighbor] = Node(neighbor.val)
                hash[n].neighbors.append(hash[neighbor])
        return hash[node]