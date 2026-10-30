class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = 201
        for s in strs:
            m = min(m, len(s))
        for ch in range(m):
            for w in range(1, len(strs)):
                if strs[w][ch] != strs[0][ch]:
                    return strs[0][:ch]
        return strs[0][:m]

        