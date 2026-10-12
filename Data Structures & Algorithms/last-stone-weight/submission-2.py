class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            s1, s2 = heapq.heappop(stones), heapq.heappop(stones)
            heapq.heappush(stones, s1 - s2)

        return -stones[0]            
