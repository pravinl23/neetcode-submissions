class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjacencyList = {}
        for i, p in enumerate(points):
            adjacencyList[i] = []
        for i, p in enumerate(points):
            for adj in adjacencyList:
                if adj == (i):
                    continue
                d = abs(points[adj][0] - p[0]) + abs(points[adj][1] - p[1])
                adjacencyList[adj].append([i, d])
    
        heap = [] # distance, node_index
        heapq.heappush(heap, [0, 0])
        res = 0
        visited = set()
        while heap:
            d, i = heapq.heappop(heap)
            if i in visited:
                    continue
            visited.add(i)
            res += d
            for nei_i, dist in adjacencyList[i]:
                if nei_i in visited:
                    continue
                heapq.heappush(heap, [dist, nei_i])

        return res
                

