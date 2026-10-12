class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap = nums
        self.k = k
        over = len(nums) - k
        for i in range(over):
            heapq.heappop(nums)

    def add(self, val: int) -> int:
        h = self.heap
        heapq.heappush(h, val)
        if len(h) > self.k:
            heapq.heappop(h)
        return h[0]
