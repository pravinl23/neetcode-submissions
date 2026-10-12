class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacency = {}
        for i in range(n):
            adjacency[i] = []

        for e in edges:
            adjacency[e[0]].append(e[1])
            adjacency[e[1]].append(e[0])
        
        visited = set()
        visiting = set()
        def containsCycles(n, prev):
            if n in visiting:
                return True
            visited.add(n)
            visiting.add(n)
            for adj in adjacency[n]:
                if adj == prev:
                    continue
                if adj in visited:
                    return True
                if containsCycles(adj, n):
                    return True
            visiting.remove(n)
            return False

        if containsCycles(0, None):
            return False
        for i in range(n):
            if i not in visited:
                return False

        return True