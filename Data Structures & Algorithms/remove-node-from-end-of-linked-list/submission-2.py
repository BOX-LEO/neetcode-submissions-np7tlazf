# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s = f = head
        for _ in range(n):
            f = f.next
        prev = None
        while f:
            prev = s
            s = s.next
            f = f.next
        if prev:
            prev.next = s.next
        else:
            head = head.next
        return head