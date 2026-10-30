class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        res = []
        for p in points:
            heapq.heappush(heap, [(p[0]**2 + p[1]**2)**0.5, p])
        
        for i in range(k):
            if not heap:
                break
            res.append(heapq.heappop(heap)[1])

        return res