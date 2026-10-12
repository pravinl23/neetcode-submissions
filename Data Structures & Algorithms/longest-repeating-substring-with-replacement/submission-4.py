class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n, l, r, m = len(s), 0, 0, 0
        if n < 2:
            return n

        count = {}
        freq = 0

        while r < n:
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            
            freq = max(freq, count[s[r]])

            if (r - l + 1) - freq > k:
                count[s[l]] -= 1
                l += 1
            
            m = max(m, r - l + 1)
            r += 1
                
        return m