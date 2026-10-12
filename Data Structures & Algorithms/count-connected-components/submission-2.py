class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacencyList = {}
        for i in range(n):
            adjacencyList[i] = []

        for e in edges:
            adjacencyList[e[0]].append(e[1])
            adjacencyList[e[1]].append(e[0])
        print(adjacencyList)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for adj in adjacencyList[node]:
                dfs(adj)

        counter = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                counter += 1

        return counter
            
                