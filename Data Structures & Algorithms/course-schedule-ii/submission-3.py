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

        def dfs(n):
            if n in visiting:
                return False
            if n in visited:
                return True
            visiting.add(n)
            for adj in adjacencyList[n]:
                if not dfs(adj):
                    return False
            visiting.remove(n)
            visited.add(n)
            res.append(n)

            return True


        for n in range(numCourses):
            if n not in visited:
                if not dfs(n):
                    return []

        return res
                
            