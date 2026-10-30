class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacencyList = {}
        for i in range(1, n + 1):
            adjacencyList[i] = []

        for t in times:
            adjacencyList[t[0]].append([t[1], t[2]])
        
        visited = set()
        heap = [(0, k)]
        res = 0
        while heap:
            distance, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            res = max(res, distance)
            for nei, weight in adjacencyList[node]:
                heapq.heappush(heap, (distance + weight, nei))
        
        
        if len(visited) == n:
            return res
        return -1