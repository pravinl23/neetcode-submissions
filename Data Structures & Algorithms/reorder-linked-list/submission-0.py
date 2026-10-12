# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # first find middle
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        slow.next = None # break it apart the 2 lists
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        back = prev
        front = head

        while back:
            tempfront = front.next
            tempback = back.next

            front.next = back
            back.next = tempfront
            
            front = tempfront
            back = tempback