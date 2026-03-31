# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        add1 = 0
        head = output = ListNode()
        while l1 or l2 or add1>0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum_v = val1+val2+add1
            add1 = sum_v//10
            sum_v = sum_v%10
            output.next = ListNode(val = sum_v)
            output= output.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next