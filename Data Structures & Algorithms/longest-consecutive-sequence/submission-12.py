class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        inList = set(nums)

        m = 0
        for n in nums:
            if (n - 1) in inList:
                continue
            running = 0
            increase = n
            while increase in inList:
                running += 1
                increase += 1
            
            m = max(m, running)
        
        return m

            