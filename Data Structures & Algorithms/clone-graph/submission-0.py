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
            return None
        hash = {}
        hash[node]=Node(node.val)
        dq = deque([node])
        while dq:
            n = dq.popleft()
            for neighbor in n.neighbors:
                if neighbor not in hash:
                    hash[neighbor] = Node(neighbor.val)
                    dq.append(neighbor)

        seen = set([node])
        dq = deque([node])
        while dq:
            n = dq.popleft()
            neighbors = []
            for neighbor in n.neighbors:
                neighbors.append(hash[neighbor])
                if neighbor not in seen:
                    dq.append(neighbor)
                    seen.add(neighbor)
            hash[n].neighbors = neighbors

        return hash[node]