class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(t)
        seek = {}
        for c in t:
            if c not in seek:
                seek[c] = 1
            else:
                seek[c] += 1
        l = 0
        m = float("inf")
        res = ""
        found = 0
        foundList = deque()


        for r in range(len(s)):
            if s[r] in seek:
                if seek[s[r]] > 0:
                    found += 1
                seek[s[r]] -= 1
                foundList.append(r)
                
            if found == n:
                while seek[s[foundList[0]]] < 0:
                    seek[s[foundList.popleft()]] += 1

                l = foundList[0]
                if (r - l + 1) < m:
                    res = s[l:r + 1]
                    m = (r - l + 1)


                seek[s[foundList.popleft()]] += 1
                found -= 1


        return res


    