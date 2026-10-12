class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = nums # heap
        heapq.heapify(self.h)
        self.k = k
        while self.h and len(self.h) > k:
            heapq.heappop(self.h)

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        if self.h and len(self.h) > self.k:
            heapq.heappop(self.h)
        return self.h[0]
