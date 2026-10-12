class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, m = 0, 0
        seen = {}
        maxFreq = 0
        
        for r in range(len(s)):
            if s[r] not in seen:
                seen[s[r]] = 0
            seen[s[r]] += 1
            maxFreq = max(maxFreq, seen[s[r]])
            if (r - l + 1) - maxFreq > k:
                seen[s[l]] -= 1
                l += 1
            
            m = max(m, r - l + 1)


        return m