class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        heapq.heappush(stones, 0)
        heapq.heappush(stones, 0)
        print(stones)

        while len(stones) > 1:
            s1, s2 = heapq.heappop(stones), heapq.heappop(stones)
            heapq.heappush(stones, min(s1,s2) - max(s1, s2))

        return -stones[0]            
