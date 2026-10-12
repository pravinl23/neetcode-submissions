class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacencyList = {}
        for i in range(numCourses):
            adjacencyList[i] = []
        for p in prerequisites:
            adjacencyList[p[0]].append(p[1])

        visited = set()
        visiting = set()
        res = []
        cycle = False

        def dfs(n):
            nonlocal cycle
            if n in visiting:
                cycle = True
                return

            visiting.add(n)

            for adj in adjacencyList[n]:
                if adj not in visited:
                    dfs(adj)
            visiting.remove(n)
            visited.add(n)
            res.append(n)


        for n in range(numCourses):
            if n not in visited:
                dfs(n)
                if cycle:
                    return []

        return res
                
            