# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        temp = head
        while temp:
            length+=1
            temp = temp.next
        half = length//2+length%2
        if length>2:        
            hr = head
            for i in range(half):
                hr=hr.next
            
            
            n = None
            right = ListNode()
            while hr.next:
                temp = hr.next
                hr.next = n
                n = hr
                hr = temp
            hr.next = n
            
            output = outputhead = ListNode()
            for _ in range(length//2):
                temp1 = head.next
                output.next = head
                output = output.next
                head = temp1


                temp2 = hr.next
                output.next = hr
                output=output.next
                hr = temp2
            if length%2==1:
                output.next = head
                output = output.next
                output.next = None
            head = outputhead.next

        

