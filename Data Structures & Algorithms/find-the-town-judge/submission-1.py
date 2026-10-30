class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        counter = {}
        for i in range(1, n + 1):
            counter[i] = 0

        for a,b in trust:
            if b in counter:
                counter[b] += 1
            if a in counter:
                del counter[a]

        for c in counter:
            if counter[c] == n - 1:
                return c
        return -1