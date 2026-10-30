# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        curr = dummy
        remainder = 0
        while l1 and l2:
            s = l1.val + l2.val + remainder
            remainder = 0
            ones = s
            if s > 9:
                ones = s % 10
                remainder = 1
            curr.next = ListNode(ones)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            s = l1.val + remainder
            remainder = 0
            ones = s
            if s > 9:
                ones = s % 10
                remainder = 1
            curr.next = ListNode(ones)
            curr = curr.next
            l1 = l1.next

        while l2:
            s = l2.val + remainder
            ones = s
            remainder = 0
            if s > 9:
                ones = s % 10
                remainder = 1
            curr.next = ListNode(ones)
            curr = curr.next
            l2 = l2.next

        if remainder > 0:
            curr.next = ListNode(remainder)

        return dummy.next
