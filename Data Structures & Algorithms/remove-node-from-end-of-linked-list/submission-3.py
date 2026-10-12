# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        front = head
        while n > 0:
            if not front:
                return None
            n -= 1
            front = front.next
        if not front:
            return head.next

        curr = head
        while front.next:
            curr = curr.next
            front = front.next

        curr.next = curr.next.next

        return head