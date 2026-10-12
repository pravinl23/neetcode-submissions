class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        seen = {}
        i = 0
        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS in seen:
                res[seen[sortedS]].append(s)
            else:
                seen[sortedS] = i
                res.append([s])
                i += 1

        return res
