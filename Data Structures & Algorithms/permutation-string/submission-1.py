class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False

        l, r = 0, len(s1) - 1

        counter = {}
        for c in ("qwertyuiopasdfghjklzxcvbnm"):
            counter[c] = 0
        for i in range(l, r + 1):
            counter[s2[i]] += 1

        goal = {}
        for c in s1:
            if c not in goal:
                goal[c] = 0
            goal[c] += 1

        while r < len(s2):
            # check if goal matches counter
            flip = True
            for key in goal:
                if goal[key] == counter[key]:
                    flip = flip and True
                else:
                    flip = False

            if flip:
                return True
            else:
                counter[s2[l]] -= 1
                r += 1
                l += 1
                if r < len(s2):
                    counter[s2[r]] += 1

        return False

            
