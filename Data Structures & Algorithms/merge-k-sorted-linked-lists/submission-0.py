# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        n = len(lists)
        done = 0
        
        # initialize the heap with first 3 nodes
        for i in range(n):
                if not lists[i]:
                    done += 1
                    continue
                currNode = lists[i]
                lists[i].next = lists[i].next
                heapq.heappush(heap, [currNode.val, i, currNode])

        head = ListNode()
        dummy = head
        while done < n:
            smallest = heapq.heappop(heap)
            dummy.next = smallest[2]
            dummy = dummy.next

            newNode = smallest[2]
            newNode = newNode.next
            if not newNode:
                done += 1
                continue
            heapq.heappush(heap, [newNode.val, smallest[1], newNode])

        return head.next
