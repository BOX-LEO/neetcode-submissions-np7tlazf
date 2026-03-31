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
        
        if list1.val>list2.val:
            list1,list2 = list2,list1
        result = list1
        head = result
        head1 = list1.next
        head2 = list2
        while head1 and head2:
            if head1.val<head2.val:
                result.next = head1
                head1 = head1.next
            else:
                result.next = head2
                head2 = head2.next
            result = result.next
        if head1:
            result.next = head1
        if head2:
            result.next = head2
        return head

            
