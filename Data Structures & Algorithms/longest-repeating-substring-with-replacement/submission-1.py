class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if not s:
            return 0
        l = r = 0
        m = 0
        seen = {}
        for c in ("QWERTYUIOPASDFGHJKLZXCVBNM"):
            seen[c] = 0
        seen[s[0]] += 1
        while r < len(s):
            maxChar = None
            maxNum = 0
            for c in seen:
                if seen[c] > maxNum:
                    maxChar = c
                    maxNum = seen[c]
            if (r - l + 1) - maxNum > k:
                seen[s[l]] -= 1
                l += 1
            else:
                m = max((r - l + 1), m)
                r += 1
                if r < len(s):
                    seen[s[r]] += 1

        return m
