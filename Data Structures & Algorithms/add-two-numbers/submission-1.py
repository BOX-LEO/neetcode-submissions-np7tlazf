# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        res = dummy_head
        carry = 0
        while l1 or l2 or carry:
            if l1 and l2:
                temp = l1.val+l2.val+carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                temp = l1.val+carry
                l1 = l1.next
            elif l2:
                temp = l2.val+carry
                l2 = l2.next
            else:
                temp = carry
            carry = temp//10
            res.next = ListNode(temp%10)
            res = res.next
        return dummy_head.next
