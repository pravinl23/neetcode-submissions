class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        a = Counter(s)
        b = Counter(t)

        for char, count in a.items():
            if char not in b:
                return False
            if b[char] != count:
                return False

        return True


