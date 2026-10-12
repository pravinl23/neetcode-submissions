class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = r = 0
        m = 0
        while r < len(s):
            if s[r] in seen:
                if seen[s[r]] >= l:
                    l = seen[s[r]] + 1
                    del seen[s[r]]

            m = max((r - l) + 1, m)
            seen[s[r]] = r
            r += 1
        return m