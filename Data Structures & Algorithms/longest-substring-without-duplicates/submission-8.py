class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        
        seen = {}
        l, r = 0, 1
        seen[s[l]] = l
        counter, m = 1, 1
        while r < n:
            if s[r] in seen:
                newl = seen[s[r]] + 1
                for i in range(l, seen[s[r]] + 1):
                    del seen[s[i]]
                    counter -= 1
                l = newl
            seen[s[r]] = r
            counter += 1
            r += 1
            m = max(m, counter)

        return m
            

        