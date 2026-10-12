class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjacencyList = {}
        degree = {}
        for w in words:
            for ch in w:
                adjacencyList[ch] = set()
                degree[ch] = 0
        
        for i in range(len(words) - 1):
            p = 0
            while p < len(words[i]) and p < len(words[i + 1]):
                if words[i][p] != words[i + 1][p]:
                    adjacencyList[words[i][p]].add(words[i + 1][p])
                    break
                p += 1
            if p == len(words[i + 1]) and len(words[i]) > len(words[i + 1]):
                return ""

        for ch in adjacencyList:
            for adj in adjacencyList[ch]:
                degree[adj] += 1
        queue = deque()
        for ch in degree:
            if degree[ch] == 0:
                queue.append(ch)
        
        res = ""
        while queue:
            curr = queue.popleft()
            res += curr
            for adj in adjacencyList[curr]:
                degree[adj] -= 1
                if degree[adj] == 0:
                    queue.append(adj)

        if len(res) == len(degree):
            return res
        return ""

        
        