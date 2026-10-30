class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        for ch in s1:
            if ch not in s1_map:
                s1_map[ch] = 0
            s1_map[ch] += 1
        
        l, r = 0, 0
        while r < len(s2):   
            if s2[r] in s1_map:
                if s1_map[s2[r]] == 0:
                    while s2[l] != s2[r]:
                        s1_map[s2[l]] += 1
                        l += 1
                    l += 1
                else:
                    s1_map[s2[r]] -= 1
            else:
                while l < r:
                    s1_map[s2[l]] += 1
                    l += 1
                l = r + 1
            r += 1
            if (r - l) == len(s1):
                return True
        return False
                    
