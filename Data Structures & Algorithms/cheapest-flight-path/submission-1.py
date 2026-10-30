class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        k_left = [0 for _ in range(n)]
        adjacencyList = {}
        for i in range(n):
            adjacencyList[i] = []
        for f in flights:
            adjacencyList[f[0]].append([f[1], f[2]])
        heap = [] # distance, k_left, node
        heapq.heappush(heap, [0, k, src])

        while heap:
            d, currk_left, n = heapq.heappop(heap)
            if n == dst and currk_left >= -1:
                return d
            if k_left[n] > currk_left:
                continue
            k_left[n] = currk_left
            for nei, dist in adjacencyList[n]:
                heapq.heappush(heap, [dist + d, currk_left - 1, nei])

        return -1
