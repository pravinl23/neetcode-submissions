# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        curr = head
        while curr and curr.next:
            p = curr.next
            v = gcd(curr.val, curr.next.val)
            curr.next = ListNode(v)
            curr.next.next = p
            curr = p
        return head

