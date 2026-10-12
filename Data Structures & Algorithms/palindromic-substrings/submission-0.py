class Solution:
    def countSubstrings(self, s: str) -> int:
        s = "#" + "#".join(s) + "#"
        n = len(s)
        counter = 0
        for i, ch in enumerate(s):
            if ch != "#":
                counter += 1
            l, r = i - 1, i + 1
            
            while 0 <= l < n and 0 <= r < n and s[l] == s[r]:
                if s[l] != "#":
                    counter += 1
                l -= 1
                r += 1
        return counter
