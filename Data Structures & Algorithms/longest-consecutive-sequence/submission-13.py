class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        inList = set(nums)

        m = 0
        for n in nums:
            if (n - 1) in inList:
                continue
            running = 0
            while n in inList:
                running += 1
                n += 1
            
            m = max(m, running)
        
        return m

            