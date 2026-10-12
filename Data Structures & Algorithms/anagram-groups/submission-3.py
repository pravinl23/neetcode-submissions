class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        res = []
        i = 0
        for s in strs:
            ss = ''.join(sorted(s))
            if ss in seen:
                res[seen[ss]].append(s)
            else:
                res.append([])
                res[i] = [s]
                seen[ss] = i
                i += 1

        return res