class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = "#" + "#".join(s) + "#"

        ans = ""
        length = 0
        n = len(s)
        for i, ch in enumerate(s):
            running = 0
            l, r = i, i
            while 0 <= l < n and 0 <= r < n and s[l] == s[r]:
                running += 1
                l -= 1
                r += 1
            if running > length:
                length = running
                ans = s[l + 1:r]
        
        return ans.replace("#", "")

            
                
