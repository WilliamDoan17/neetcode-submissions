# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2 = list1, list2 
        dummy = ListNode()
        c = dummy

        while c1 and c2:
            if c1.val < c2.val:
                c.next = ListNode(c1.val)
                c1 = c1.next
            else:
               c.next = ListNode(c2.val)  
               c2 = c2.next
            c = c.next
        
        while c1:
            c.next = ListNode(c1.val)
            c1 = c1.next
            c = c.next
        
        while c2:
            c.next = ListNode(c2.val)
            c2 = c2.next
            c = c.next

        return dummy.next