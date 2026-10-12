class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.length = 0
        self.min_length = 0
        self.max_length = 0

    def addNum(self, num: int) -> None:
        if self.length == 0:
            heapq.heappush(self.min_heap, num)
            self.min_length += 1
            self.length += 1
            return

        m = self.findMedian()

        if num > m:
            heapq.heappush(self.min_heap, num)
            self.min_length += 1
        else:
            heapq.heappush(self.max_heap, -num)
            self.max_length += 1
    
        self.length += 1
        if abs(self.max_length - self.min_length) < 2:
            return

        if self.max_length > self.min_length:
            popped = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -popped)
            self.max_length -= 1
            self.min_length += 1
        else:
            popped = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -popped)
            self.max_length += 1
            self.min_length -= 1
        return
        
    def findMedian(self) -> float:
        if self.length % 2 == 0:
            return (-self.max_heap[0] + self.min_heap[0]) / 2

        if self.max_length > self.min_length:
            return -self.max_heap[0]

        return self.min_heap[0]