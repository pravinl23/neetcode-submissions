class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        seen = {}
        i = 0
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)
            if key in seen:
                res[seen[key]].append(s)
            else:
                seen[key] = i
                res.append([s])
                i += 1

        return res
