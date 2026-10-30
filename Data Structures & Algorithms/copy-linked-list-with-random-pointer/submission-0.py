"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        i = 0
        actual = []
        nodes = {}
        curr = head
        while curr:
            actual.append(curr.val)
            curr.val = i
            nodes[i] = Node(i)
            curr = curr.next
            i += 1

        curr = head
        dummy = Node(0)
        dummyHead = dummy
        while curr:
            dummyHead.next = nodes[curr.val]
            dummyHead = dummyHead.next
            if curr.random:
                dummyHead.random = nodes[curr.random.val]
            curr = curr.next

        for i in nodes:
            nodes[i].val = actual[i]
        
        return dummy.next

        