class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjacencyList = {}
        for i in range(1, len(edges) + 1):
            adjacencyList[i] = []
        for e1, e2 in edges:
            adjacencyList[e1].append(e2)
            adjacencyList[e2].append(e1)
        
        res = None
        path = []
        def dfs(n, prev):
            nonlocal res
            if n in path:
                if not res: res = path[path.index(n):]
                return
            path.append(n)
            for nei in adjacencyList[n]:
                if nei == prev:
                    continue 
                dfs(nei, n)
            path.remove(n)


        dfs(len(edges), 0)
        res = set(res)
        for i in range(len(edges) - 1, -1, -1):
            if edges[i][0] in res and edges[i][1] in res:
                return edges[i]
