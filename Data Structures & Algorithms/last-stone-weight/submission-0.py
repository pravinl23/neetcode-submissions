class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) >= 2:
            s1 = heapq.heappop_max(stones)
            s2 = heapq.heappop_max(stones)
            if s1 == s2:
                continue
            elif s1 > s2:
                heapq.heappush_max(stones, s1 - s2)
            else:
                heapq.heappush_max(stones, s2 - s1)
        
        if stones:
            return stones[0]
        else:
            return 0

            