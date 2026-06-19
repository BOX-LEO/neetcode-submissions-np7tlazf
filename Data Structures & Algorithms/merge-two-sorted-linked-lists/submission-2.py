# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        h1,h2 = list1,list2
        dummy_head = ListNode()
        cur = dummy_head
        while h1 and h2:
            if h1.val<=h2.val:
                cur.next = ListNode(h1.val)
                h1 = h1.next
            else:
                cur.next = ListNode(h2.val)
                h2 = h2.next
            cur = cur.next
        if h1:
            cur.next = h1
        elif h2:
            cur.next = h2
        return dummy_head.next
        
        