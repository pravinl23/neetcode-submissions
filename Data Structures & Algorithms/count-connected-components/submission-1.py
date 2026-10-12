class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacencyList = {}
        for i in range(n):
            adjacencyList[i] = []

        for e in edges:
            adjacencyList[e[0]].append(e[1])
            adjacencyList[e[1]].append(e[0])
        print(adjacencyList)
        
        visiting = set()
        visited = set()
        def dfs(node, prev):
            if node in visiting:
                return
            visiting.add(node)

            for adj in adjacencyList[node]:
                if adj in visited:
                    continue
                if prev == adj:
                    continue
                dfs(adj, node)

            visited.add(node)

        counter = 0
        for i in range(n):
            if i not in visited:
                dfs(i, None)
                counter += 1

        return counter
            
                