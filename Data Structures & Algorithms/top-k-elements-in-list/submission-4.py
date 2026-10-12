class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)
        numHeap = []
        for num, count in a.items():
            heapq.heappush(numHeap, (-count, num))

        res = []
        for i in range(k):
            res.append(heapq.heappop(numHeap)[1])
        return res