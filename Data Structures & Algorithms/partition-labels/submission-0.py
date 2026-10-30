class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        c = Counter(s)
        res = []
        l, r = 0, 0
        visiting = set()
        while r < len(s): 
            visiting.add(s[r])
            c[s[r]] -= 1
            if c[s[r]] == 0:
                visiting.remove(s[r])
            if not visiting:
                res.append(r - l + 1)
                l = r + 1
            r += 1

        return res                
