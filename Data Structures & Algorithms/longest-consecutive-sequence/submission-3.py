class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqset = set(nums)

        maxsofar = 1
        if len(nums) == 0:
            return 0
        for n in nums:
            if (n - 1) in seqset:
                continue
            else:
                currlen = 1
                i = n + 1
                while i in seqset:
                    currlen += 1
                    i = i + 1
                maxsofar = max(currlen, maxsofar)

        
        return maxsofar
