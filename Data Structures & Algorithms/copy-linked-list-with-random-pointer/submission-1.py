"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_table = {None:None}
        cur = head
        while cur:
            hash_table[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            hash_table[cur].next = hash_table[cur.next]
            hash_table[cur].random = hash_table[cur.random]
            cur = cur.next
        return hash_table[head]