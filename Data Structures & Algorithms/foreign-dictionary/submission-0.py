class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjacencyList = {}
        for i in range(len(words) - 1):
            a,b = 0,0
            while a < len(words[i]) and b < len(words[i + 1]):
                if words[i][a] != words[i + 1][b]:
                    if words[i][a] not in adjacencyList:
                        adjacencyList[words[i][a]] = set()
                    adjacencyList[words[i][a]].add(words[i + 1][b])
                    break
                else:
                    a += 1
                    b += 1
            if a == len(words[i + 1]) and len(words[i]) > len(words[i + 1]):
                return ""

        print(adjacencyList)
        unique = 0
        degree = {}
        for w in words:
            for ch in w:
                if ch not in degree:
                    degree[ch] = 0
                    unique += 1

        for ch in adjacencyList:
            for adj in adjacencyList[ch]:
                degree[adj] += 1
        print(degree)
        queue = deque()
        for ch in degree:
            if degree[ch] == 0:
                queue.append(ch)
        
        res = ""
        while queue:
            curr = queue.popleft()
            res += curr
            if curr not in adjacencyList:
                continue
            for adj in adjacencyList[curr]:
                degree[adj] -= 1
                if degree[adj] == 0:
                    queue.append(adj)

        print(unique, degree)
        print(res)
        if len(res) == unique:
            return res
        return ""

        
        