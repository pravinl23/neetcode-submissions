# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        head = ListNode(0, head)
        l = head
        r = head
        c = 0
        while r:
            r = r.next
            c += 1

        n = c - n
        for i in range(n - 1):
            l = l.next

        l.next = l.next.next
        return head.next

