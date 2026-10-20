# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def helper(self, head: Optional[ListNode], start: int, end: int) -> List[ListNode]:
        if end - start == 2:
            return [head, head.next]
        elif end - start == 1:
            return [head, head] 
        inner = self.helper(head.next, start + 1, end - 1)
        head.next = inner[1].next
        inner[1].next = inner[1].next.next
        head.next.next = inner[0]
        return [head, inner[1]]


    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        l = 0
        while cur:
            l += 1
            cur = cur.next
        if l == 0:
            return None
        head = self.helper(head, 0, l)[0]