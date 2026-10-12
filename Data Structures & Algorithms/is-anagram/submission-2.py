class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dps = {}
        dpt = {}
        if (len(s) != len(t)):
            return False
        for i in range(len(t)):
            if s[i] in dps:
                dps[s[i]] += 1
            else:
                dps[s[i]] = 1
            if t[i] in dpt:
                dpt[t[i]] += 1
            else:
                dpt[t[i]] = 1
                
        
        return dps == dpt